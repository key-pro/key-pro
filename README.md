<div align="center">

<a href="https://trade-information.laravel.cloud/">
  <img src="assets/header.gif" alt="Kamimura Yuki。Laravel で投資分析サイトを公開" width="100%">
</a>

<img src="https://readme-typing-svg.demolab.com?font=Noto+Sans+JP&weight=600&size=22&duration=2800&pause=700&color=67E8F9&center=true&vCenter=true&width=980&height=48&lines=%E7%94%BB%E9%9D%A2%E3%81%AB%E5%BC%B5%E3%82%8A%E4%BB%98%E3%81%8B%E3%81%AA%E3%81%84%E3%80%81%E5%A4%9C5%E5%88%86%E3%81%AE%E6%A0%AA%E5%BC%8F%E3%83%81%E3%82%A7%E3%83%83%E3%82%AF;1%E6%97%A51%E5%9B%9E%E6%9B%B4%E6%96%B0%E3%80%82%E3%83%87%E3%82%A4%E3%83%88%E3%83%AC%E3%81%AF%E4%B8%8D%E8%A6%81%E3%81%A7%E3%81%99;%E4%BC%9A%E5%93%A1%E7%99%BB%E9%8C%B2%E3%81%AF%E7%84%A1%E6%96%99%E3%81%A7%E3%81%99;%E5%BA%83%E5%91%8A%E3%81%AF%E3%81%AA%E3%81%8F%E3%80%81%E8%AA%AD%E3%82%80%E4%BA%BA%E3%81%AE%E5%AF%84%E4%BB%98%E3%81%A7%E7%B6%9A%E3%81%84%E3%81%A6%E3%81%84%E3%81%BE%E3%81%99" alt="画面に張り付かない、夜5分の株式チェック">

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
知っている会社の株価を、仕事終わりの夜5分で見比べられるようにしています。公開しているサイトは Laravel、分析用の画面は Python で作っています。

<div align="center">

<img src="assets/features.gif" alt="夜5分、終値、対円レート、会員機能、銘柄一覧、寄付が切り替わる" width="100%">

</div>

## 公開中のサイト

**[trade-information](https://trade-information.laravel.cloud/)** は、画面の題は「投資分析」、ロゴの横は「夜5分」です。画面に張り付かない、夜5分の株式チェックです。デイトレのような秒単位の売買は不要で、仕事終わりに1日1回更新の株価を見ます。2026年に Laravel で公開しました。会員登録は無料です。売買の推奨ではありません。広告は載せず、[読む人の寄付](https://trade-information.laravel.cloud/donate)で続けています。寄付しなくても、使える機能は同じです。

### 非会員機能（登録・ログイン不要）

ログインなしですぐに閲覧・利用できます。世界の相場環境の把握から個別銘柄の検索・簡易分析まで行えます。

| 機能 | 仕様・できること |
| --- | --- |
| 世界マーケット相場 | 日経平均・TOPIX・NYダウ・S&P500・為替・米10年債利回り・原油・金など世界主要市場の相場ボード。グリッド表示とヒートマップ表示の切替、リアルタイム連動、市場カテゴリ別フィルタ（日本市場、米国市場、為替・仮想通貨、商品・金利）に対応 |
| 世界情勢ニュース＆トレード分析レーダー | 世界の重要ニュースをリアルタイム解析。マクロ地合いセンチメントゲージ（地合いスコア / リスクオフ・中立・リスクオン）、今夜の概況、注目テーマチップ、ニュースごとの市場影響・トレード戦略・影響指標バッジを表示 |
| 銘柄一覧・検索 | [10,477銘柄](https://trade-information.laravel.cloud/Meigara)を企業名・日本語名・証券コードから検索（/ キー対応、リアルタイムサジェスト）。38市場（日本・米国・中国・欧州各国・南米・オセアニア・中東・アフリカ等）の国別フィルタ、テーマ別（高配当、メガバンク、商社、半導体、自動車、通信、米国テック、米国ETF）絞り込み |
| 終値・騰落チェック | その日の取引が終わったときの終値と前日比騰落を表示（取得不可時は「終値なし」）。一覧ページごとの値動き集計（上昇・下落・変わらず銘柄数、平均騰落率、最大上昇・下落銘柄） |
| お試し銘柄閲覧 | 登録不要で代表銘柄（トヨタ 7203、三菱UFJ 8306、NTT 9432、Apple AAPL、Microsoft MSFT）の終値、日足推移グラフ、配当利回り、PER、PBR、期間高値・安値、100株（1単元）買付時の必要資金・年間配当目安、過去配当推移を確認可能 |
| 表示カスタマイズ | 昼（ライト）と夜（ダーク）のテーマ切替。投資家モード（初心者・NISA・中級者・上級者）の選択および診断質問（ヒアリング） |
| 寄付・規約 | 広告なし運営を支える任意のStripe寄付（毎月 500円/1,000円/3,000円、1回寄付 100円〜）、利用規約、プライバシーポリシー、免責事項、特定商取引法に基づく表記 |

### 会員機能（無料登録・要ログイン）

会員登録は無料です。パスワードは使わず、メールのログインリンク、パスキー（WebAuthn）、または Google アカウントでログインできます。

| 機能 | 仕様・できること |
| --- | --- |
| 銘柄の詳細・チャート | 全10,477銘柄の個別日足グラフ。日ごとの終値推移チャート、テクニカル指標、ファンダメンタルズ指標を詳細確認 |
| 為替（FX）マーケット | 円との交換レート推移。26通貨ペアの終値、前日比変動率、スパークライン、トレンド・オシレーター各種指標による詳細分析 |
| 取引ルールガイド | 初心者や新NISA向けに、日本株・米国株の取引時間、受渡日（T+1/T+2）、夜間取引、成長投資枠のルール、今夜の市場状況を整理 |
| ウォッチリスト | 気になる銘柄を登録・管理。「今夜の確認（Tonight）」フラグによる日々のチェック、ウォッチリストから銘柄比較へのワンクリック連携 |
| ポートフォリオ（保有記録） | 保有銘柄の株数・取得単価・現在価格を記録し、評価損益や取得金額割合を自動計算・可視化 |
| 投資メモ | 銘柄ごとに購入理由、目標価格・見直し価格、取引の気付きを保存 |
| 銘柄比較 | 最大4銘柄の株価・騰落・配当利回り・PERなどを横並びで比較。比較セットの保存・呼び出し |
| 資金計画シミュレーター | 投資資金と買付希望価格から買付可能株数や必要金額を自動計算（売買推奨ではなく試算） |
| 100種類の専門分析ツール | 配当利回り、割安度チェック（PER）、1年と1か月の配当予測、買うのに必要な金額など、初心者向け基本4ツールから高度な専門分析まで100種類の計算ツール群 |
| マイページ・データ管理 | 今夜チェックした銘柄の確認状況、手元の記録（ウォッチ・保有・メモ）のサマリー表示、登録データの一括エクスポート（バックアップ） |

株価は1日に1回更新します。日本株は平日の夕方（取引終了後）に反映され、取引の途中の気配は含みません。この1日分を、日足と呼びます。日本株以外の株価と、通貨の交換レートも、その日の終わりの値段（終値）です。板情報や分足は出していません。このサイトは、1日の終わりの値段を見る場所です。投資助言や、売買の勧誘は行いません。

寄付は任意で、会員機能や投資助言の対価ではありません。毎月は 500円、1,000円、3,000円です。1回は決済画面で 100円から指定でき、最初の表示は 1,000円です。毎月は、次回の請求より前に止められます。使途は、相場データの取得と、このサイトの運営費です。受付期間の定めはありません。金額によって、見える機能は変わりません。[特定商取引法に基づく表記](https://trade-information.laravel.cloud/tokushoho)を置いています。

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
| 公開サイト | Laravel、PHP。会員ログインはメールリンク、パスキー、または外部アカウント |
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
| 2026 | [trade-information](https://trade-information.laravel.cloud/) を Laravel でリリース。画面の題は投資分析、ロゴの横は夜5分。夜5分、1日1回の株式チェック。世界マーケット相場・世界情勢ニュースレーダーを搭載。日足グラフ・FX・ウォッチ・保有・比較・分析ツール100種は会員。広告は載せず、寄付で続けている |

<div align="center">

<img src="https://raw.githubusercontent.com/key-pro/key-pro/output/github-contribution-grid-snake-dark.svg" alt="コントリビューションをなぞるスネーク" width="100%">

<img src="https://github-readme-stats.vercel.app/api?username=key-pro&show_icons=true&include_all_commits=true&locale=ja&hide_border=true&bg_color=060a12&title_color=67e8f9&icon_color=2dd4bf&text_color=e2e8f0" alt="GitHub stats" height="170">
<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=key-pro&layout=compact&locale=ja&hide_border=true&langs_count=6&bg_color=060a12&title_color=67e8f9&text_color=e2e8f0" alt="Top languages" height="170">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:060a12,100:22d3ee&height=80&section=footer&fontSize=1&text=&desc=" alt="" width="100%">

</div>
