# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""檢查 data/team_season.csv。

刻意不重用 etl.py：這裡用 regex 自己重新解析 raw/，才能抓到 ETL 的解析錯誤。

執行：uv run work/validate.py [--seed N]
"""

from __future__ import annotations

import argparse
import csv
import html
import random
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "raw"
DATA = ROOT / "data"
PCT_TOL = 0.0011  # 官網勝率四捨五入到小數第三位

failures: list[str] = []


def check(ok: bool, label: str) -> None:
    print(f"  [{'OK' if ok else 'FAIL'}] {label}")
    if not ok:
        failures.append(label)


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


# ---- 獨立的 raw 解析 ----

def cells(tr: str) -> list[str]:
    return [html.unescape(re.sub(r"<[^>]+>", "", c)).strip()
            for c in re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", tr, re.S)]


def table_rows(text: str) -> list[str]:
    return re.findall(r"<tr>(.*?)</tr>", text, re.S)


def raw_standing(year: int, code: str) -> dict[str, float]:
    text = (RAW / f"standings_{year}.html").read_text(encoding="utf-8")
    full = text.split('record_table_caption">全年戰績')[1]
    rows = table_rows(full)
    header = cells(rows[0])
    for tr in rows[1:]:
        if f"TeamNo={code}" in tr:
            c = cells(tr)
            w, t, l = map(int, c[header.index("勝-和-敗")].split("-"))
            return {"games": int(c[header.index("出賽數")]), "wins": w, "ties": t,
                    "losses": l, "win_pct": float(c[header.index("勝率")])}
    raise KeyError((year, code))


def raw_players(kind: str, year: int, code: str) -> list[dict[str, str]]:
    text = (RAW / f"team_{kind}_{year}_{code}.html").read_text(encoding="utf-8")
    rows = table_rows(text)
    header = cells(rows[0])
    return [dict(zip(header, cells(tr))) for tr in rows[1:] if "acnt=" in tr]


def raw_value(field: str, year: int, code: str) -> float:
    if field in ("games", "wins", "losses", "ties", "win_pct"):
        return raw_standing(year, code)[field]
    bat = raw_players("batting", year, code)
    pit = raw_players("pitching", year, code)
    total = lambda rows, col: sum(int(r[col]) for r in rows)
    if field == "runs_scored":
        return total(bat, "得分")
    if field == "runs_allowed":
        return total(pit, "失分")
    if field == "hits":
        return total(bat, "安打")
    if field == "home_runs":
        return total(bat, "全壘打")
    if field == "batting_avg":
        return round(total(bat, "安打") / total(bat, "打數"), 3)
    if field == "era":
        outs = sum(int(ip) * 3 + int(f or 0)
                   for ip, _, f in (r["投球局數"].partition(".") for r in pit))
        return round(total(pit, "自責分") * 27 / outs, 2)
    raise ValueError(field)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", type=int, default=random.randrange(10**6))
    args = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")  # Windows 主控台預設不是 UTF-8

    season = read_csv(DATA / "team_season.csv")
    mapping = read_csv(DATA / "team_mapping.csv")

    def code_for(team: str, year: int) -> str:
        (m,) = [m for m in mapping if m["team"] == team
                and int(m["first_year"]) <= year <= int(m["last_year"])]
        return m["club_code"]

    print(f"1. 隨機抽 5 個數字和 raw/ 核對（seed={args.seed}）")
    rng = random.Random(args.seed)
    numeric = [f for f in season[0] if f not in ("year", "team")]
    for _ in range(5):
        row, field = rng.choice(season), rng.choice(numeric)
        year = int(row["year"])
        code = code_for(row["team"], year)
        got, want = float(row[field]), raw_value(field, year, code)
        check(abs(got - want) < 1e-9,
              f"{year} {row['team']}({code}) {field}: csv={row[field]} raw={want}")

    print("2. 每列 wins+losses+ties = games；win_pct = wins/(wins+losses)")
    bad_sum = [r for r in season
               if int(r["wins"]) + int(r["losses"]) + int(r["ties"]) != int(r["games"])]
    bad_pct = [r for r in season
               if abs(float(r["win_pct"]) - int(r["wins"]) / (int(r["wins"]) + int(r["losses"]))) > PCT_TOL]
    check(not bad_sum, f"勝+敗+和=出賽數（{len(season)} 列，不符 {len(bad_sum)}）")
    check(not bad_pct, f"勝率誤差 ≤ {PCT_TOL}（不符 {len(bad_pct)}）")
    for r in bad_sum + bad_pct:
        print("     ", r)

    print("3. 每年全聯盟 總勝場 = 總敗場")
    by_year: dict[int, list[dict[str, str]]] = defaultdict(list)
    for r in season:
        by_year[int(r["year"])].append(r)
    for year, rows in sorted(by_year.items()):
        w = sum(int(r["wins"]) for r in rows)
        l = sum(int(r["losses"]) for r in rows)
        check(w == l, f"{year}: {len(rows)} 隊，勝 {w} / 敗 {l}")

    print("4. 額外檢查")
    for year, rows in sorted(by_year.items()):
        rs = sum(int(r["runs_scored"]) for r in rows)
        ra = sum(int(r["runs_allowed"]) for r in rows)
        check(rs == ra, f"{year}: 全聯盟得分 {rs} = 失分 {ra}")
    check(all(int(r["year"]) >= 2021 for r in season if r["team"] == "味全龍"), "味全龍 沒有 2021 年以前的列")
    check(all(int(r["year"]) >= 2024 for r in season if r["team"] == "台鋼雄鷹"), "台鋼雄鷹 沒有 2024 年以前的列")
    check(len({(r["year"], r["team"]) for r in season}) == len(season), "（year, team）沒有重複")

    print()
    if failures:
        print(f"FAILED: {len(failures)} 項")
        sys.exit(1)
    print("ALL PASSED")


if __name__ == "__main__":
    main()
