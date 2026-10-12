# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "beautifulsoup4>=4.12",
# ]
# ///
"""把 raw/ 的中華職棒官網原始 HTML 轉成 data/ 下的整齊 CSV（不修改 raw/）。

輸出：
  data/team_season.csv   每隊每年一列（一軍例行賽全年）
  data/team_mapping.csv  球隊代碼／歷年隊名 → 現名對照

執行：uv run work/etl.py
"""

from __future__ import annotations

import csv
import re
from collections import defaultdict
from pathlib import Path

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "raw"
DATA = ROOT / "data"
YEARS = range(2015, 2026)

# 官網用三碼 ClubNo 區分球團；球團易主時代碼會換，這裡把舊代碼接到現在的代碼。
SUCCESSOR = {
    "AJK": "AJL",  # Lamigo桃猿 → 2020 起 樂天桃猿
    "AEM": "AEO",  # 義大犀牛   → 2017 起 富邦悍將
}
# 官網戰績表只寫簡稱，網頁顯示舊名時用完整隊名。
FULL_NAME = {
    "Lamigo": "Lamigo桃猿",
    "義大": "義大犀牛",
}

FIELDS = [
    "year", "team", "games", "wins", "losses", "ties", "win_pct",
    "runs_scored", "runs_allowed", "hits", "home_runs", "batting_avg", "era",
]


def soup(path: Path) -> BeautifulSoup:
    return BeautifulSoup(path.read_text(encoding="utf-8"), "html.parser")


def club_code(href: str) -> str:
    return re.search(r"TeamNo=([A-Z]{3})", href).group(1)


def parse_standings(year: int) -> list[dict]:
    """取「全年戰績」表；每列必須有球隊連結，其他列（表頭、空白）都略過。"""
    doc = soup(RAW / f"standings_{year}.html")
    caption = doc.find("div", class_="record_table_caption", string="全年戰績")
    table = caption.find_parent("div", class_="RecordTableWrap").find("table")
    header = [th.get_text(strip=True) for th in table.find("tr").find_all("th")]
    i_games, i_wlt, i_pct = header.index("出賽數"), header.index("勝-和-敗"), header.index("勝率")

    out = []
    for tr in table.find_all("tr")[1:]:
        link = tr.find("a", href=re.compile(r"TeamNo="))
        if link is None:
            continue
        cells = [td.get_text(strip=True) for td in tr.find_all("td")]
        wins, ties, losses = (int(n) for n in cells[i_wlt].split("-"))  # 官網格式是 勝-和-敗
        out.append({
            "year": year,
            "code": club_code(link["href"]),
            "source_name": link.get_text(strip=True),
            "games": int(cells[i_games]),
            "wins": wins,
            "losses": losses,
            "ties": ties,
            "win_pct": f"{float(cells[i_pct]):.3f}",
        })
    return out


def player_rows(path: Path) -> list[dict[str, str]]:
    """球員明細列。以「有球員連結」判斷，排除合計列與空白列；
    但保留官網漏了姓名、仍有球員連結的列（例如 2022 中信兄弟 acnt=0000006837）。"""
    table = soup(path).find("table")
    trs = table.find_all("tr")
    header = [th.get_text(strip=True) for th in trs[0].find_all("th")]
    rows = []
    for tr in trs[1:]:
        if tr.find("a", href=re.compile(r"/team/person\?acnt=")) is None:
            continue
        cells = [td.get_text(strip=True) for td in tr.find_all("td")]
        rows.append(dict(zip(header, cells)))
    return rows


def innings_to_outs(ip: str) -> int:
    """投球局數 '5.1' 代表 5又1/3 局 → 16 個出局數。"""
    whole, _, frac = ip.partition(".")
    return int(whole) * 3 + int(frac or 0)


def team_stats(year: int, code: str) -> dict:
    bat = player_rows(RAW / f"team_batting_{year}_{code}.html")
    pit = player_rows(RAW / f"team_pitching_{year}_{code}.html")
    at_bats = sum(int(r["打數"]) for r in bat)
    hits = sum(int(r["安打"]) for r in bat)
    outs = sum(innings_to_outs(r["投球局數"]) for r in pit)
    earned = sum(int(r["自責分"]) for r in pit)
    return {
        "runs_scored": sum(int(r["得分"]) for r in bat),
        "runs_allowed": sum(int(r["失分"]) for r in pit),
        "hits": hits,
        "home_runs": sum(int(r["全壘打"]) for r in bat),
        "batting_avg": f"{hits / at_bats:.3f}",
        "era": f"{earned * 27 / outs:.2f}",  # 自責分 × 9 ÷ (出局數 / 3)
    }


def main() -> None:
    standings = [row for y in YEARS for row in parse_standings(y)]

    # 現名 = 現任代碼在最近一年出現的名稱
    latest_name: dict[str, str] = {}
    for row in sorted(standings, key=lambda r: r["year"]):
        latest_name[row["code"]] = row["source_name"]

    def current(code: str) -> str:
        return latest_name[SUCCESSOR.get(code, code)]

    # 對照表：每個 (代碼, 官網名稱) 一列，記錄出現年份
    seen: dict[tuple[str, str], list[int]] = defaultdict(list)
    for row in standings:
        seen[(row["code"], row["source_name"])].append(row["year"])
    mapping = []
    for (code, name), years in sorted(seen.items(), key=lambda kv: (current(kv[0][0]), min(kv[1]))):
        team = current(code)
        display = team if name == team else f"{team}（{FULL_NAME.get(name, name)}）"
        mapping.append({
            "club_code": code,
            "source_name": name,
            "team": team,
            "display_name": display,
            "first_year": min(years),
            "last_year": max(years),
        })

    out = []
    for row in standings:
        out.append({
            "year": row["year"],
            "team": current(row["code"]),
            **{k: row[k] for k in ("games", "wins", "losses", "ties", "win_pct")},
            **team_stats(row["year"], row["code"]),
        })
    out.sort(key=lambda r: (r["year"], r["team"]))

    DATA.mkdir(exist_ok=True)
    write_csv(DATA / "team_season.csv", FIELDS, out)
    write_csv(DATA / "team_mapping.csv", list(mapping[0]), mapping)
    print(f"team_season.csv: {len(out)} rows, team_mapping.csv: {len(mapping)} rows")


def write_csv(path: Path, fields: list[str], rows: list[dict]) -> None:
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    main()
