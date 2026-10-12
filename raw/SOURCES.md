# 原始資料來源 (SOURCES)

- 來源：中華職棒大聯盟全球資訊網 https://www.cpbl.com.tw
- 賽別：一軍例行賽（`Kindcode/KindCode=A`）
- 年份：2015–2025
- 下載方式：curl，每次請求間隔 2 秒；檔案為伺服器回應的原始 HTML，未經修改。

## 重要說明

這些頁面的資料表是由瀏覽器按下「查詢」後用 AJAX **POST** 載入的。每個檔案存的是該 POST 的原始回應，也就是頁面上 `#PageListContainer` 內的 HTML 片段，不是完整網頁。
每次 POST 也都附帶 `__RequestVerificationToken`（防偽 token，與 session cookie 綁定），下表不列出。

| 檔案類型 | 瀏覽器可見頁面 | 資料端點 (POST) | 內容 |
|---|---|---|---|
| `standings_YYYY.html` | https://www.cpbl.com.tw/standings/history | `/standings/historyaction` | 上半季、下半季、全年戰績（出賽數、勝-和-敗、勝率、勝差、對戰、主客場） |
| `team_batting_YYYY_CLUB.html` | https://www.cpbl.com.tw/team/teamscore?ClubNo=CLUB | `/team/teamscoreaction`（`Position=01` 打擊成績） | 該隊當年所有球員打擊成績（得分、安打、全壘打、打數、打擊率…） |
| `team_pitching_YYYY_CLUB.html` | https://www.cpbl.com.tw/team/teamscore?ClubNo=CLUB | `/team/teamscoreaction`（`Position=02` 投球成績） | 該隊當年所有投手成績（投球局數、失分、自責分、防禦率…） |

官網沒有提供歷年的「團隊合計」表（`/standings/season` 的團隊打擊/投球表只有本季資料）。所以團隊數據只能用球員明細加總：
得分、安打、全壘打、失分直接加總；打擊率 = 安打 ÷ 打數；防禦率 = 自責分 × 9 ÷ 投球局數（局數的 `.1`、`.2` 分別代表 1/3、2/3 局）。
驗證結果：每年全聯盟的打擊「得分」總和等於投手「失分」總和。

球隊代碼：ACN 中信兄弟、ADD 統一7-ELEVEn獅、AJK Lamigo（2015–2019）、AJL 樂天桃猿（2020–）、AEM 義大（2015–2016）、AEO 富邦悍將（2017–）、AAA 味全龍（2021–）、AKP 台鋼雄鷹（2024–）。

## 檔案清單

| 檔案 | 下載日期 | 請求 | POST 參數 | HTTP | 位元組 |
|---|---|---|---|---|---|
| standings_2015.html | 2026-10-12 | POST https://www.cpbl.com.tw/standings/historyaction | `Kindcode=A&Year=2015&ExecAction=&IndexOfPages=0` | 200 | 19574 |
| standings_2016.html | 2026-10-12 | POST https://www.cpbl.com.tw/standings/historyaction | `Kindcode=A&Year=2016&ExecAction=&IndexOfPages=0` | 200 | 19566 |
| standings_2017.html | 2026-10-12 | POST https://www.cpbl.com.tw/standings/historyaction | `Kindcode=A&Year=2017&ExecAction=&IndexOfPages=0` | 200 | 19611 |
| standings_2018.html | 2026-10-12 | POST https://www.cpbl.com.tw/standings/historyaction | `Kindcode=A&Year=2018&ExecAction=&IndexOfPages=0` | 200 | 19605 |
| standings_2019.html | 2026-10-12 | POST https://www.cpbl.com.tw/standings/historyaction | `Kindcode=A&Year=2019&ExecAction=&IndexOfPages=0` | 200 | 19602 |
| standings_2020.html | 2026-10-12 | POST https://www.cpbl.com.tw/standings/historyaction | `Kindcode=A&Year=2020&ExecAction=&IndexOfPages=0` | 200 | 19642 |
| standings_2021.html | 2026-10-12 | POST https://www.cpbl.com.tw/standings/historyaction | `Kindcode=A&Year=2021&ExecAction=&IndexOfPages=0` | 200 | 24607 |
| standings_2022.html | 2026-10-12 | POST https://www.cpbl.com.tw/standings/historyaction | `Kindcode=A&Year=2022&ExecAction=&IndexOfPages=0` | 200 | 24606 |
| standings_2023.html | 2026-10-12 | POST https://www.cpbl.com.tw/standings/historyaction | `Kindcode=A&Year=2023&ExecAction=&IndexOfPages=0` | 200 | 24605 |
| standings_2024.html | 2026-10-12 | POST https://www.cpbl.com.tw/standings/historyaction | `Kindcode=A&Year=2024&ExecAction=&IndexOfPages=0` | 200 | 30048 |
| standings_2025.html | 2026-10-12 | POST https://www.cpbl.com.tw/standings/historyaction | `Kindcode=A&Year=2025&ExecAction=&IndexOfPages=0` | 200 | 30022 |
| team_batting_2015_ACN.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=ACN&KindCode=A&Year=2015&Position=01&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 62809 |
| team_pitching_2015_ACN.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=ACN&KindCode=A&Year=2015&Position=02&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 55133 |
| team_batting_2015_ADD.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=ADD&KindCode=A&Year=2015&Position=01&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 55731 |
| team_pitching_2015_ADD.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=ADD&KindCode=A&Year=2015&Position=02&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 46871 |
| team_batting_2015_AEM.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=AEM&KindCode=A&Year=2015&Position=01&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 50383 |
| team_pitching_2015_AEM.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=AEM&KindCode=A&Year=2015&Position=02&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 51833 |
| team_batting_2015_AJK.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=AJK&KindCode=A&Year=2015&Position=01&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 55729 |
| team_pitching_2015_AJK.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=AJK&KindCode=A&Year=2015&Position=02&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 56770 |
| team_batting_2016_ACN.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=ACN&KindCode=A&Year=2016&Position=01&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 53942 |
| team_pitching_2016_ACN.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=ACN&KindCode=A&Year=2016&Position=02&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 51841 |
| team_batting_2016_ADD.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=ADD&KindCode=A&Year=2016&Position=01&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 57494 |
| team_pitching_2016_ADD.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=ADD&KindCode=A&Year=2016&Position=02&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 46870 |
| team_batting_2016_AEM.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=AEM&KindCode=A&Year=2016&Position=01&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 52177 |
| team_pitching_2016_AEM.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=AEM&KindCode=A&Year=2016&Position=02&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 46852 |
| team_batting_2016_AJK.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=AJK&KindCode=A&Year=2016&Position=01&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 61064 |
| team_pitching_2016_AJK.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=AJK&KindCode=A&Year=2016&Position=02&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 56765 |
| team_batting_2017_ACN.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=ACN&KindCode=A&Year=2017&Position=01&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 57507 |
| team_pitching_2017_ACN.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=ACN&KindCode=A&Year=2017&Position=02&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 53457 |
| team_batting_2017_ADD.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=ADD&KindCode=A&Year=2017&Position=01&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 61056 |
| team_pitching_2017_ADD.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=ADD&KindCode=A&Year=2017&Position=02&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 53504 |
| team_batting_2017_AEO.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=AEO&KindCode=A&Year=2017&Position=01&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 57499 |
| team_pitching_2017_AEO.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=AEO&KindCode=A&Year=2017&Position=02&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 51834 |
| team_batting_2017_AJK.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=AJK&KindCode=A&Year=2017&Position=01&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 55720 |
| team_pitching_2017_AJK.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=AJK&KindCode=A&Year=2017&Position=02&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 41891 |
| team_batting_2018_ACN.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=ACN&KindCode=A&Year=2018&Position=01&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 53925 |
| team_pitching_2018_ACN.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=ACN&KindCode=A&Year=2018&Position=02&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 46860 |
| team_batting_2018_ADD.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=ADD&KindCode=A&Year=2018&Position=01&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 61046 |
| team_pitching_2018_ADD.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=ADD&KindCode=A&Year=2018&Position=02&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 51832 |
| team_batting_2018_AEO.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=AEO&KindCode=A&Year=2018&Position=01&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 55715 |
| team_pitching_2018_AEO.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=AEO&KindCode=A&Year=2018&Position=02&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 53479 |
| team_batting_2018_AJK.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=AJK&KindCode=A&Year=2018&Position=01&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 59254 |
| team_pitching_2018_AJK.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=AJK&KindCode=A&Year=2018&Position=02&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 43557 |
| team_batting_2019_ACN.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=ACN&KindCode=A&Year=2019&Position=01&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 55705 |
| team_pitching_2019_ACN.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=ACN&KindCode=A&Year=2019&Position=02&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 46874 |
| team_batting_2019_ADD.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=ADD&KindCode=A&Year=2019&Position=01&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 68184 |
| team_pitching_2019_ADD.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=ADD&KindCode=A&Year=2019&Position=02&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 61757 |
| team_batting_2019_AEO.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=AEO&KindCode=A&Year=2019&Position=01&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 52163 |
| team_pitching_2019_AEO.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=AEO&KindCode=A&Year=2019&Position=02&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 56771 |
| team_batting_2019_AJK.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=AJK&KindCode=A&Year=2019&Position=01&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 52160 |
| team_pitching_2019_AJK.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=AJK&KindCode=A&Year=2019&Position=02&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 46868 |
| team_batting_2020_ACN.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=ACN&KindCode=A&Year=2020&Position=01&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 46823 |
| team_pitching_2020_ACN.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=ACN&KindCode=A&Year=2020&Position=02&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 41904 |
| team_batting_2020_ADD.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=ADD&KindCode=A&Year=2020&Position=01&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 57494 |
| team_pitching_2020_ADD.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=ADD&KindCode=A&Year=2020&Position=02&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 55133 |
| team_batting_2020_AEO.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=AEO&KindCode=A&Year=2020&Position=01&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 53936 |
| team_pitching_2020_AEO.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=AEO&KindCode=A&Year=2020&Position=02&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 48496 |
| team_batting_2020_AJL.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=AJL&KindCode=A&Year=2020&Position=01&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 52142 |
| team_pitching_2020_AJL.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=AJL&KindCode=A&Year=2020&Position=02&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 53465 |
| team_batting_2021_AAA.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=AAA&KindCode=A&Year=2021&Position=01&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 61035 |
| team_pitching_2021_AAA.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=AAA&KindCode=A&Year=2021&Position=02&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 51824 |
| team_batting_2021_ACN.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=ACN&KindCode=A&Year=2021&Position=01&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 59268 |
| team_pitching_2021_ACN.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=ACN&KindCode=A&Year=2021&Position=02&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 51798 |
| team_batting_2021_ADD.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=ADD&KindCode=A&Year=2021&Position=01&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 66363 |
| team_pitching_2021_ADD.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=ADD&KindCode=A&Year=2021&Position=02&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 48497 |
| team_batting_2021_AEO.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=AEO&KindCode=A&Year=2021&Position=01&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 66377 |
| team_pitching_2021_AEO.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=AEO&KindCode=A&Year=2021&Position=02&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 60054 |
| team_batting_2021_AJL.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=AJL&KindCode=A&Year=2021&Position=01&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 53917 |
| team_pitching_2021_AJL.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=AJL&KindCode=A&Year=2021&Position=02&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 55135 |
| team_batting_2022_AAA.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=AAA&KindCode=A&Year=2022&Position=01&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 59268 |
| team_pitching_2022_AAA.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=AAA&KindCode=A&Year=2022&Position=02&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 53443 |
| team_batting_2022_ACN.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=ACN&KindCode=A&Year=2022&Position=01&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 59256 |
| team_pitching_2022_ACN.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=ACN&KindCode=A&Year=2022&Position=02&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 55116 |
| team_batting_2022_ADD.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=ADD&KindCode=A&Year=2022&Position=01&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 66400 |
| team_pitching_2022_ADD.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=ADD&KindCode=A&Year=2022&Position=02&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 51821 |
| team_batting_2022_AEO.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=AEO&KindCode=A&Year=2022&Position=01&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 77061 |
| team_pitching_2022_AEO.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=AEO&KindCode=A&Year=2022&Position=02&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 51822 |
| team_batting_2022_AJL.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=AJL&KindCode=A&Year=2022&Position=01&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 59244 |
| team_pitching_2022_AJL.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=AJL&KindCode=A&Year=2022&Position=02&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 51802 |
| team_batting_2023_AAA.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=AAA&KindCode=A&Year=2023&Position=01&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 57498 |
| team_pitching_2023_AAA.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=AAA&KindCode=A&Year=2023&Position=02&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 55104 |
| team_batting_2023_ACN.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=ACN&KindCode=A&Year=2023&Position=01&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 57467 |
| team_pitching_2023_ACN.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=ACN&KindCode=A&Year=2023&Position=02&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 60069 |
| team_batting_2023_ADD.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=ADD&KindCode=A&Year=2023&Position=01&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 66364 |
| team_pitching_2023_ADD.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=ADD&KindCode=A&Year=2023&Position=02&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 53496 |
| team_batting_2023_AEO.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=AEO&KindCode=A&Year=2023&Position=01&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 68154 |
| team_pitching_2023_AEO.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=AEO&KindCode=A&Year=2023&Position=02&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 51806 |
| team_batting_2023_AJL.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=AJL&KindCode=A&Year=2023&Position=01&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 55702 |
| team_pitching_2023_AJL.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=AJL&KindCode=A&Year=2023&Position=02&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 58413 |
| team_batting_2024_AAA.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=AAA&KindCode=A&Year=2024&Position=01&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 61068 |
| team_pitching_2024_AAA.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=AAA&KindCode=A&Year=2024&Position=02&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 48502 |
| team_batting_2024_ACN.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=ACN&KindCode=A&Year=2024&Position=01&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 66323 |
| team_pitching_2024_ACN.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=ACN&KindCode=A&Year=2024&Position=02&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 48503 |
| team_batting_2024_ADD.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=ADD&KindCode=A&Year=2024&Position=01&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 64578 |
| team_pitching_2024_ADD.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=ADD&KindCode=A&Year=2024&Position=02&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 56784 |
| team_batting_2024_AEO.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=AEO&KindCode=A&Year=2024&Position=01&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 61053 |
| team_pitching_2024_AEO.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=AEO&KindCode=A&Year=2024&Position=02&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 56785 |
| team_batting_2024_AJL.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=AJL&KindCode=A&Year=2024&Position=01&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 52136 |
| team_pitching_2024_AJL.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=AJL&KindCode=A&Year=2024&Position=02&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 53450 |
| team_batting_2024_AKP.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=AKP&KindCode=A&Year=2024&Position=01&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 50358 |
| team_pitching_2024_AKP.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=AKP&KindCode=A&Year=2024&Position=02&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 56815 |
| team_batting_2025_AAA.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=AAA&KindCode=A&Year=2025&Position=01&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 53940 |
| team_pitching_2025_AAA.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=AAA&KindCode=A&Year=2025&Position=02&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 51807 |
| team_batting_2025_ACN.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=ACN&KindCode=A&Year=2025&Position=01&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 57444 |
| team_pitching_2025_ACN.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=ACN&KindCode=A&Year=2025&Position=02&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 58414 |
| team_batting_2025_ADD.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=ADD&KindCode=A&Year=2025&Position=01&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 59240 |
| team_pitching_2025_ADD.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=ADD&KindCode=A&Year=2025&Position=02&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 55133 |
| team_batting_2025_AEO.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=AEO&KindCode=A&Year=2025&Position=01&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 64589 |
| team_pitching_2025_AEO.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=AEO&KindCode=A&Year=2025&Position=02&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 53485 |
| team_batting_2025_AJL.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=AJL&KindCode=A&Year=2025&Position=01&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 59223 |
| team_pitching_2025_AJL.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=AJL&KindCode=A&Year=2025&Position=02&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 50152 |
| team_batting_2025_AKP.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=AKP&KindCode=A&Year=2025&Position=01&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 61006 |
| team_pitching_2025_AKP.html | 2026-10-12 | POST https://www.cpbl.com.tw/team/teamscoreaction | `ClubNo=AKP&KindCode=A&Year=2025&Position=02&DefendStation=&ExecAction=&IndexOfPages=0&Sortby=01` | 200 | 51822 |
