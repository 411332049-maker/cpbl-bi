# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""把 data/ 的 CSV 轉成 docs/data.js，讓 docs/index.html 直接雙擊（file://）就能打開。

瀏覽器在 file:// 下不能用 fetch() 讀 CSV/JSON，所以改成 JS 檔設定全域變數：
  <script src="data.js"></script>  →  window.CPBL_DATA

執行：uv run work/build_data.py
"""

from __future__ import annotations

import csv
import json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
OUT = ROOT / "docs" / "data.js"

INT_FIELDS = {"year", "games", "wins", "losses", "ties", "runs_scored", "runs_allowed",
              "hits", "home_runs", "first_year", "last_year"}
FLOAT_FIELDS = {"win_pct", "batting_avg", "era"}


def read_csv(path: Path) -> list[dict]:
    with path.open(encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    for row in rows:
        for k, v in row.items():
            if k in INT_FIELDS:
                row[k] = int(v)
            elif k in FLOAT_FIELDS:
                row[k] = float(v)
    return rows


def main() -> None:
    seasons = read_csv(DATA / "team_season.csv")
    mapping = read_csv(DATA / "team_mapping.csv")

    # 每列加上當年應顯示的名稱，例如 2015 樂天桃猿 → 「樂天桃猿（Lamigo桃猿）」
    for row in seasons:
        (m,) = [m for m in mapping
                if m["team"] == row["team"] and m["first_year"] <= row["year"] <= m["last_year"]]
        row["display_name"] = m["display_name"]

    payload = {
        "generated": date.today().isoformat(),
        "source": "中華職棒大聯盟全球資訊網 https://www.cpbl.com.tw（一軍例行賽）",
        "teamSeason": seasons,
        "teamMapping": mapping,
    }
    OUT.parent.mkdir(exist_ok=True)
    body = json.dumps(payload, ensure_ascii=False, indent=1)
    OUT.write_text(f"// 由 work/build_data.py 產生，請勿手動修改\nwindow.CPBL_DATA = {body};\n",
                   encoding="utf-8")
    print(f"{OUT.relative_to(ROOT)}: {len(seasons)} seasons, {len(mapping)} mappings, "
          f"{OUT.stat().st_size:,} bytes")


if __name__ == "__main__":
    main()
