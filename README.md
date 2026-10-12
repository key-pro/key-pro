<div align="center">

<a href="https://trade-information.laravel.cloud/">
  <img src="assets/header.gif" alt="Kamimura Yuki。Laravel で投資分析サイトを公開" width="100%">
</a>

<img src="https://readme-typing-svg.demolab.com?font=Noto+Sans+JP&weight=600&size=22&duration=2800&pause=700&color=67E8F9&center=true&vCenter=true&width=980&height=48&lines=%E7%9F%A5%E3%81%A3%E3%81%A6%E3%81%84%E3%82%8B%E4%BC%9A%E7%A4%BE%E3%81%AE%E6%A0%AA%E4%BE%A1%E3%82%92%E3%80%81%E5%A4%9C%E3%81%AB%E4%B8%80%E5%BA%A6%E8%A6%8B%E3%82%8B;%E5%B9%B3%E6%97%A5%E3%81%AE%E5%A4%95%E6%96%B9%E3%80%811%E6%97%A51%E5%9B%9E%E3%80%825%E5%88%86%E3%81%A7%E8%B6%B3%E3%82%8A%E3%81%BE%E3%81%99;%E4%BC%9A%E5%93%A1%E7%99%BB%E9%8C%B2%E3%81%AF%E7%84%A1%E6%96%99%E3%81%A7%E3%81%99;%E5%BA%83%E5%91%8A%E3%81%AF%E3%81%AA%E3%81%8F%E3%80%81%E8%AA%AD%E3%82%80%E4%BA%BA%E3%81%AE%E5%AF%84%E4%BB%98%E3%81%A7%E7%B6%9A%E3%81%84%E3%81%A6%E3%81%84%E3%81%BE%E3%81%99" alt="知っている会社の株価を、夜に一度見る">

<br>

<a href="https://trade-information.laravel.cloud/"><img alt="trade-information" src="https://img.shields.io/badge/LIVE-trade--information-2DD4BF?style=for-the-badge&logo=laravel&logoColor=0b1220"></a>
<a href="https://github.com/key-pro/streamlit"><img alt="FX dashboard" src="https://img.shields.io/badge/FX-Streamlit-67E8F9?style=for-the-badge&logo=python&logoColor=0b1220"></a>
<a href="https://github.com/key-pro/PDF_Integration_App"><img alt="PDF" src="https://img.shields.io/badge/PDF-Integration-94A3B8?style=for-the-badge&logo=adobeacrobatreader&logoColor=0b1220"></a>

<br><br>

<img src="https://skillicons.dev/icons?i=laravel,php,python,django,docker,mysql,react,ts,java&theme=dark" alt="Laravel, PHP, Python, Django, Docker, MySQL, React, TypeScript, Java">

<img src="assets/marquee.gif" alt="Laravel、PHP、Python、Streamlit、Django、Docker、React、TypeScript、Java が流れる" width="100%">
<img src="assets/equalizer.gif" alt="高低が入れ替わるバー" width="100%">

</div>

Kamimura Yuki です。
知っている会社の株価を、仕事終わりに1日1回だけ見比べられるようにしています。公開しているサイトは Laravel、分析用の画面は Python で作っています。

<div align="center">

<img src="assets/features.gif" alt="日足、対円レート、テクニカル、会員機能、スクリーナー、寄付が切り替わる" width="100%">

</div>

## 公開中のサイト

**[trade-information](https://trade-information.laravel.cloud/)** は、画面では投資分析と出しています。知っている会社の株価を、夜に一度見るサイトです。トヨタやソニー、Appleのように、名前を知っている銘柄を並べ、配当と騰落を自分で見比べます。仕事が終わったあと、1日1回、5分見れば足ります。2026年に Laravel で公開しました。会員登録は無料です。売買の推奨ではありません。広告は載せず、[読む人の寄付](https://trade-information.laravel.cloud/donate)で続けています。寄付しなくても、使える機能は同じです。

ログインなしで見られます。銘柄一覧は、会員登録なしで開けます。

| | |
| --- | --- |
| 銘柄一覧 | 知っている会社の、その日の株価です。前日より上がったか下がったかも並びます。[14,524銘柄](https://trade-information.laravel.cloud/Meigara)で、企業名・日本語名・証券コードから探せます。絞り込みは日本株と米国株です |
| 終値 | その日の取引が終わったときの株価です。騰落は、前日より上がったか下がったかです。取れない銘柄は「終値なし」と出します |
| 日本株 | 平日の夕方（取引終了後）に、その日の株価が更新されます |
| 米国株 | 米国の銘柄は、ドル建ての、その日の終わりの株価です |

サイト紹介では、トヨタ自動車、ソニーグループ、Apple、Microsoft の終値が出ます。インデックスの積立を続けたまま、高配当の株や、知っている大企業を見てみたいときに使います。毎日開く必要はありません。

まず使う計算は3つです。分析ツールは50種類あります。

| | |
| --- | --- |
| 配当金の計算 | 持っている株から、1年と、1か月あたりの配当の目安を出します |
| 割安さの目安 | 株価が利益の何倍か（PER）を見て、高いか安いかの目安にします |
| 買うのに必要な金額 | その株を買うのに、いくらかかるかを出します |

会員になると使えます。会員登録は無料です。登録のあと、次の機能が使えます。チャート、FX、取引ルール、ウォッチリスト、保有記録、銘柄比較は会員限定です。

| | |
| --- | --- |
| 銘柄の詳細 | 一覧は誰でも見られます。1日ごとの値動きのグラフ（日足）は、会員登録すると開けます |
| 為替 | 円との交換レートです。1日の終わりのレートを見ます |
| 取引ルール | 株式とFXの取引時間、決済、銘柄コードです |
| ウォッチ | 見たい銘柄を保存して、比較へ進めます |
| 保有 | 取得金額の割合と損益を残せます |
| 投資メモ | 買った理由と、あとで見返す値段を書き残せます |
| 銘柄比較 | 知っている会社の株価と配当を並べます |
| 資金計画 | 使えるお金から、買える株数の目安を出します |
| 分析ツール | 最初は、配当金、割安さの目安、買うのに必要な金額の3つです。計算は全部で50種類あります |
| 入り方 | パスワードは使わず、メールのログインリンク、パスキー、Google |

株価は1日に1回更新します。日本株は平日の夕方（取引終了後）に反映され、取引の途中の気配は含みません。この1日分を、日足と呼びます。日本株以外の株価と、通貨の交換レートも、その日の終わりの値段（終値）です。板の情報や、分ごとの値動きはありません。夜に一度見れば足ります。投資助言や、売買の勧誘は行いません。

寄付は会員画面で、1回または毎月です。毎月はあとから止められます。金額によって、見える機能は変わりません。

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
| 2026 | [trade-information](https://trade-information.laravel.cloud/) を Laravel でリリース。画面の名前は投資分析。知っている会社の株価を、平日の夕方に1日1回見る。日足のグラフは会員。広告は載せず、寄付で続けている |

<div align="center">

<img src="https://raw.githubusercontent.com/key-pro/key-pro/output/github-contribution-grid-snake-dark.svg" alt="コントリビューションをなぞるスネーク" width="100%">

<img src="https://github-readme-stats.vercel.app/api?username=key-pro&show_icons=true&include_all_commits=true&locale=ja&hide_border=true&bg_color=060a12&title_color=67e8f9&icon_color=2dd4bf&text_color=e2e8f0" alt="GitHub stats" height="170">
<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=key-pro&layout=compact&locale=ja&hide_border=true&langs_count=6&bg_color=060a12&title_color=67e8f9&text_color=e2e8f0" alt="Top languages" height="170">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:060a12,100:22d3ee&height=80&section=footer&fontSize=1&text=&desc=" alt="" width="100%">

</div>
