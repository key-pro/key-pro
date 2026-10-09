<div align="center">

<a href="https://trade-information.laravel.cloud">
  <img src="assets/header.gif" alt="Kamimura Yuki。Laravel で投資分析サイトを公開" width="100%">
</a>

<img src="https://readme-typing-svg.demolab.com?font=Noto+Sans+JP&weight=600&size=22&duration=2800&pause=700&color=67E8F9&center=true&vCenter=true&width=980&height=48&lines=%E6%97%A5%E8%B6%B3%E3%82%92%E3%80%81%E3%81%B2%E3%81%A8%E3%81%A4%E3%81%AE%E7%94%BB%E9%9D%A2%E3%81%A7%E8%A6%8B%E6%AF%94%E3%81%B9%E3%82%8B;%E4%BC%9A%E5%93%A1%E7%99%BB%E9%8C%B2%E3%81%AF%E7%84%A1%E6%96%99%E3%81%A7%E3%81%99;%E6%8A%95%E8%B3%87%E3%83%A1%E3%83%A2%E3%81%A8%E3%80%81%E8%B3%87%E9%87%91%E8%A8%88%E7%94%BB%E3%81%8C%E4%BD%BF%E3%81%88%E3%81%BE%E3%81%99;%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%8A%E3%83%BC%E3%81%AF%2014%2C524%20%E9%8A%98%E6%9F%84%E3%80%82%E6%97%A5%E6%9C%AC%E6%A0%AA%E3%81%A8%E7%B1%B3%E5%9B%BD%E6%A0%AA" alt="日足を、ひとつの画面で見比べる">

<br>

<a href="https://trade-information.laravel.cloud/Meigara"><img alt="trade-information" src="https://img.shields.io/badge/LIVE-trade--information-2DD4BF?style=for-the-badge&logo=laravel&logoColor=0b1220"></a>
<a href="https://github.com/key-pro/streamlit"><img alt="FX dashboard" src="https://img.shields.io/badge/FX-Streamlit-67E8F9?style=for-the-badge&logo=python&logoColor=0b1220"></a>
<a href="https://github.com/key-pro/PDF_Integration_App"><img alt="PDF" src="https://img.shields.io/badge/PDF-Integration-94A3B8?style=for-the-badge&logo=adobeacrobatreader&logoColor=0b1220"></a>

<br><br>

<img src="https://skillicons.dev/icons?i=laravel,php,python,django,docker,mysql,react,ts,java&theme=dark" alt="Laravel, PHP, Python, Django, Docker, MySQL, React, TypeScript, Java">

<img src="assets/marquee.gif" alt="Laravel、PHP、Python、Streamlit、Django、Docker、React、TypeScript、Java が流れる" width="100%">
<img src="assets/equalizer.gif" alt="高低が入れ替わるバー" width="100%">

</div>

Kamimura Yuki です。
日本株から海外株、為替まで、日足とテクニカルを一つの画面で見比べられるようにしています。公開しているサイトは Laravel、分析用の画面は Python で作っています。

<div align="center">

<img src="assets/features.gif" alt="日足、対円レート、テクニカル、会員機能、スクリーナー、寄付が切り替わる" width="100%">

</div>

## 公開中のサイト

**[trade-information](https://trade-information.laravel.cloud/Meigara)** は、2026年にリリースした投資分析サイトです。日本株と海外市場の日足と、為替・テクニカルを同じ画面で見比べられます。会員登録は無料です。スクリーナーは誰でも使え、銘柄の詳細、為替、取引ルール、ウォッチ、保有、投資メモ、銘柄比較、資金計画、分析ツールはログインすると使えます。株価は日足です。日本株は営業日の大引け後に更新され、取引中の気配は含みません。広告は載せず、[読む人の寄付](https://trade-information.laravel.cloud/donate)で続けています。寄付しなくても、使える機能は同じです。

| | |
| --- | --- |
| スクリーナー | 14,524銘柄。企業名と証券コードで検索し、日本株と米国株で絞り込み。一覧からチャートへ進める |
| 日足 | 日本株は営業日の大引け後に更新。米国株はドル建ての終値。画面では FMP 対応とも表示 |
| 為替 | 対円レートと、通貨ペアの日足（会員向け） |
| 銘柄の詳細 | 四本値、日足チャート、テクニカル判断、ファンダメンタルズ（会員向け） |
| 会員向け | ウォッチ、保有、投資メモ（スタンス、目標、損切り）、銘柄比較、資金計画（許容損失から株数）、分析50。為替と取引ルールも含む |
| 入り方 | 会員登録は無料。パスワードは使わず、メールのログインリンク、パスキー、Google |
| 更新 | 株価は日足。日本株は大引け後。日本株以外と通貨ペアは終値。板・分足・リアルタイムはない |
| 運営 | 広告なし。寄付は会員画面で、1回または毎月。毎月はあとから止められる。見える機能は変わらない |

| 地域 | 市場 |
| --- | --- |
| アジア | 日本株 |
| アメリカ | 米国株 |

<img src="assets/divider.gif" alt="" width="100%">

## 分析用に作った画面

**[FX 為替マーケットダッシュボード](https://github.com/key-pro/streamlit)** は、Streamlit で作った手元用の分析画面です。`yfinance` から為替を取り、26通貨ペアをタイルで並べます。各タイルには価格、変動率、スパークラインがあり、そこから詳細へ進めます。米国株版は `main_us_stocks.py` から起動します。データには約15〜20分の遅れがあります。

| 分類 | 見られるもの |
| --- | --- |
| トレンド | SMA(20/50)、EMA(20)、ボリンジャーバンド、一目均衡表、DMI/ADX、パラボリックSAR、エンベロープ |
| オシレーター | RSI(14)、MACD、ストキャスティクス、サイコロジカルライン、RCI、移動平均乖離率、ヒストリカル・ボラティリティ |
| そのほか | ローソク足、フィボナッチ、ダブルボトム / ダブルトップや三尊の目視用表示、ダークとライトの切替 |

通貨ペアは、メジャー、クロス円、ユーロクロス、その他の4グループです。画面は `utils` でデータ取得と指標計算、`components` でチャートとゲージに分けています。

## 手元で使うツール

**[PDF統合ソフト](https://github.com/key-pro/PDF_Integration_App)**  
Tkinter の画面に PDF をドロップすると、ファイル名の数字順に並べて1つに結合します。PyInstaller で exe にできます。

**[Django + Docker](https://github.com/key-pro/Django_docker)**  
株価の取得と、scikit-learn による回帰を Django REST framework に載せた構成です。MySQL、Gunicorn、Docker Compose で動かします。

## 技術の使い分け

| 用途 | 技術 |
| --- | --- |
| 公開サイト | Laravel、PHP。会員ログインはメールリンク、パスキー、Google |
| 分析画面 | Python、Streamlit、pandas、Plotly、yfinance |
| API と実行環境 | Django REST framework、Docker、MySQL |
| 画面の基礎 | React、TypeScript、styled-components、Java |

<img src="assets/divider.gif" alt="" width="100%">

## これまで

| 時期 | 内容 |
| --- | --- |
| 2022 | Django でブログ（[firstProject](https://github.com/key-pro/firstProject)）と、アカウント・カテゴリ付きの写真投稿（[photoProject](https://github.com/key-pro/photoProject)）。[React + TypeScript](https://github.com/key-pro/react-typescript-app) の画面演習。Java で[電卓](https://github.com/key-pro/java-calculator)、[デスクトップアプリ](https://github.com/key-pro/java_application)、[Web システム](https://github.com/key-pro/java_websystem)。[Video.js](https://github.com/key-pro/Video.js-Yes-improvement) の改善前後を並べた比較 |
| 2024 | Todo、メモ、電卓、ゲームを PHP / Python / JavaScript / C# で書き分け（[Training_data_2024](https://github.com/key-pro/Training_data_2024)）。株価アプリを Django と Docker に載せる |
| 2025 | PDF を結合するデスクトップアプリ。FX と米国株の Streamlit ダッシュボード |
| 2026 | [trade-information](https://trade-information.laravel.cloud/Meigara) を Laravel でリリース。会員登録は無料。スクリーナーは日本株と米国株。会員は投資メモ、資金計画、分析50。広告は載せず、寄付で続けている |

<div align="center">

<img src="https://raw.githubusercontent.com/key-pro/key-pro/output/github-contribution-grid-snake-dark.svg" alt="コントリビューションをなぞるスネーク" width="100%">

<img src="https://github-readme-stats.vercel.app/api?username=key-pro&show_icons=true&include_all_commits=true&locale=ja&hide_border=true&bg_color=060a12&title_color=67e8f9&icon_color=2dd4bf&text_color=e2e8f0" alt="GitHub stats" height="170">
<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=key-pro&layout=compact&locale=ja&hide_border=true&langs_count=6&bg_color=060a12&title_color=67e8f9&text_color=e2e8f0" alt="Top languages" height="170">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:060a12,100:22d3ee&height=80&section=footer&fontSize=1&text=&desc=" alt="" width="100%">

</div>
