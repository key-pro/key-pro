<div align="center">

<a href="https://trade-information.laravel.cloud/Meigara">
  <img src="assets/header.gif" alt="Kamimura Yuki。Laravel で投資分析サイトを公開" width="100%">
</a>

<img src="https://readme-typing-svg.demolab.com?font=Noto+Sans+JP&weight=600&size=22&duration=3200&pause=900&color=67E8F9&center=true&vCenter=true&width=980&height=48&lines=%E6%97%A5%E6%9C%AC%E3%83%BB%E7%B1%B3%E5%9B%BD%E3%83%BB%E9%A6%99%E6%B8%AF%E3%83%BB%E8%8B%B1%E5%9B%BD%E3%83%BB%E3%83%89%E3%82%A4%E3%83%84%E3%83%BB%E3%82%AB%E3%83%8A%E3%83%80%E3%81%AE%E6%97%A5%E8%B6%B3%E3%82%92%E4%B8%80%E8%A6%A7%E3%81%A7%E3%81%8D%E3%81%BE%E3%81%99;%E7%B4%841.9%E4%B8%87%E9%8A%98%E6%9F%84%E3%82%92%E3%80%81%E3%82%B3%E3%83%BC%E3%83%89%E3%82%84%E4%BC%81%E6%A5%AD%E5%90%8D%E3%81%A7%E6%8E%A2%E3%81%9B%E3%81%BE%E3%81%99;%E9%8A%98%E6%9F%84%E8%A9%B3%E7%B4%B0%E3%83%BBFX%E3%83%BB%E5%8F%96%E5%BC%95%E3%83%AB%E3%83%BC%E3%83%AB%E3%81%AF%E4%BC%9A%E5%93%A1%E5%90%91%E3%81%91%E3%81%A7%E3%81%99;%E3%83%AD%E3%82%B0%E3%82%A4%E3%83%B3%E3%81%AF%E3%83%A1%E3%83%BC%E3%83%AB%E3%83%AA%E3%83%B3%E3%82%AF%E3%80%81%E3%83%91%E3%82%B9%E3%82%AD%E3%83%BC%E3%80%81Apple%E3%80%81Google" alt="日本・米国・香港・英国・ドイツ・カナダの日足を一覧できます">

<br>

<a href="https://trade-information.laravel.cloud/Meigara"><img alt="trade-information" src="https://img.shields.io/badge/LIVE-trade--information-2DD4BF?style=for-the-badge&logo=laravel&logoColor=0b1220"></a>
<a href="https://github.com/key-pro/streamlit"><img alt="FX dashboard" src="https://img.shields.io/badge/FX-Streamlit-67E8F9?style=for-the-badge&logo=python&logoColor=0b1220"></a>
<a href="https://github.com/key-pro/PDF_Integration_App"><img alt="PDF" src="https://img.shields.io/badge/PDF-Integration-94A3B8?style=for-the-badge&logo=adobeacrobatreader&logoColor=0b1220"></a>

<br><br>

<img src="https://skillicons.dev/icons?i=laravel,php,python,django,docker,mysql,react,ts,java&theme=dark" alt="Laravel, PHP, Python, Django, Docker, MySQL, React, TypeScript, Java">

</div>

日本在住の Kamimura Yuki です。日本株から海外株、為替まで、日足とテクニカルを一つの画面で見比べられるようにしています。公開しているサイトは Laravel、分析用の画面は Python で作っています。

## 公開中のサイト

**[trade-information](https://trade-information.laravel.cloud/Meigara)** は、2026年にリリースした投資分析サイトです。銘柄一覧は誰でも検索でき、銘柄の詳細・FX・取引ルールは会員向けです。

| | |
| --- | --- |
| 掲載 | 18,931銘柄。日本、米国、香港、英国、ドイツ、カナダの日足 |
| 探し方 | コードと企業名。アジア / アメリカ / 欧州で絞り込み |
| 会員向け | 銘柄ごとのテクニカル判断、購入金額の試算、主要為替レート、市場の取引ルール |
| 入り方 | パスワードは使わず、メールのログインリンク、パスキー、Apple、Google |
| データ | J-Quants、Alpha Vantage、Open Exchange Rates、Google |

| 地域 | 市場 |
| --- | --- |
| アジア | 日本株、香港株 |
| アメリカ | 米国株、カナダ株 |
| 欧州 | 英国株、ドイツ株 |

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
| 公開サイト | Laravel、PHP。会員ログインはメールリンク、パスキー、Apple、Google |
| 分析画面 | Python、Streamlit、pandas、Plotly、yfinance |
| API と実行環境 | Django REST framework、Docker、MySQL |
| 画面の基礎 | React、TypeScript、styled-components、Java |

## これまで

| 時期 | 内容 |
| --- | --- |
| 2022 | Django でブログ（[firstProject](https://github.com/key-pro/firstProject)）と、アカウント・カテゴリ付きの写真投稿（[photoProject](https://github.com/key-pro/photoProject)）。[React + TypeScript](https://github.com/key-pro/react-typescript-app) の画面演習。Java で[電卓](https://github.com/key-pro/java-calculator)、[デスクトップアプリ](https://github.com/key-pro/java_application)、[Web システム](https://github.com/key-pro/java_websystem)。[Video.js](https://github.com/key-pro/Video.js-Yes-improvement) の改善前後を並べた比較 |
| 2024 | Todo、メモ、電卓、ゲームを PHP / Python / JavaScript / C# で書き分け（[Training_data_2024](https://github.com/key-pro/Training_data_2024)）。株価アプリを Django と Docker に載せる |
| 2025 | PDF を結合するデスクトップアプリ。FX と米国株の Streamlit ダッシュボード |
| 2026 | [trade-information](https://trade-information.laravel.cloud/Meigara) を Laravel でリリース。6市場の日足を一覧し、詳細と為替は会員向け |

<div align="center">

<img src="https://github-readme-stats.vercel.app/api?username=key-pro&show_icons=true&include_all_commits=true&locale=ja&hide_border=true&bg_color=060a12&title_color=67e8f9&icon_color=2dd4bf&text_color=e2e8f0" alt="GitHub stats" height="170">
<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=key-pro&layout=compact&locale=ja&hide_border=true&langs_count=6&bg_color=060a12&title_color=67e8f9&text_color=e2e8f0" alt="Top languages" height="170">

</div>
