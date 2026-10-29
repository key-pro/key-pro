<div align="center">

<a href="https://trade-information.laravel.cloud/">
  <img src="assets/header.gif" alt="Kamimura Yuki。Laravel で投資分析サイトを公開" width="100%">
</a>

<img src="https://readme-typing-svg.demolab.com?font=Noto+Sans+JP&weight=600&size=22&duration=2800&pause=700&color=67E8F9&center=true&vCenter=true&width=980&height=48&lines=%E7%94%BB%E9%9D%A2%E3%81%AB%E5%BC%B5%E3%82%8A%E4%BB%98%E3%81%8B%E3%81%AA%E3%81%84%E3%80%81%E5%A4%9C5%E5%88%86%E3%81%AE%E6%A0%AA%E5%BC%8F%E3%83%81%E3%82%A7%E3%83%83%E3%82%AF;1%E6%97%A51%E5%9B%9E%E6%9B%B4%E6%96%B0%E3%80%82%E3%83%87%E3%82%A4%E3%83%88%E3%83%AC%E3%81%AF%E4%B8%8D%E8%A6%81%E3%81%A7%E3%81%99;%E4%BC%9A%E5%93%A1%E7%99%BB%E9%8C%B2%E3%81%AF%E7%84%A1%E6%96%99%E3%81%A7%E3%81%99;%E3%81%99%E3%81%B9%E3%81%A6%E3%81%AE%E5%9F%BA%E6%9C%AC%E6%A9%9F%E8%83%BD%E3%82%92%E7%84%A1%E6%96%99%E3%81%A7%E5%88%A9%E7%94%A8%E3%81%A7%E3%81%8D%E3%81%BE%E3%81%99" alt="画面に張り付かない、夜5分の株式チェック">

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

<img src="assets/features.gif" alt="夜5分、終値、対円レート、会員機能、銘柄一覧、分析ツール100種が切り替わる" width="100%">

</div>

## 公開中のサイト

**[trade-information](https://trade-information.laravel.cloud/)** は、画面の題は「投資分析」、ロゴの横は「夜5分」です。画面に張り付かない、夜5分の株式チェックです。デイトレのような秒単位の売買は不要で、仕事終わりに落ち着いて確認できる、1日1回更新のシンプルな分析サイトです。2026年に Laravel 13（PHP 8.5）で公開しました。会員登録を含め、すべての基本機能を無料で利用できます。売買の推奨ではありません。サイトの維持・運営には広告配信（Google AdSense）および任意の[投げ銭（開発支援）](https://trade-information.laravel.cloud/tip)を活用しています。支援の有無にかかわらず、使える機能は同じです。

### 非会員機能（登録・ログイン不要）

ログインなしですぐに閲覧・利用できます。世界の相場環境の把握から個別銘柄の検索・株価/配当プレビュー、市場取引ルール、100種類の分析計算ツールまで登録不要で公開しています。

| 機能 | 仕様・できること |
| --- | --- |
| 世界マーケット相場 | 日米主要株価指数・先物・為替・暗号資産・コモディティ・債券利回りを網羅した相場ボード（日経平均、TOPIX、日経平均先物、東証グロース250、NYダウ、S&P500、NASDAQ100、SOX指数、ドル円、ユーロ円、ユーロドル、BTC/USD、WTI原油、金先物、米10年債利回り、日10年債利回り）。グリッド表示とヒートマップ表示の切替、リアルタイム連動、市場カテゴリ別フィルタ（日本市場、米国市場、為替・暗号資産、商品・金利）、各指数のミニスパークラインチャート、為替ペアから個別詳細への直接連携に対応 |
| 世界情勢ニュース＆トレード分析レーダー | 世界の重要ニュースをリアルタイム解析。マクロ地合いセンチメントゲージ（地合いスコア 0〜100 / 極度のリスクオフ・中立・リスクオン）、今夜の概況、注目テーマチップ（米長期金利、中東情勢・原油、為替介入警戒等）、カテゴリ別絞り込み（地政学・エネルギー、金融政策・金利、為替・介入、テック・半導体）。ニュースごとのセンチメントバッジ、相場への影響と具体的な【トレード戦略】解説、影響市場・指標バッジ（急反発、安全買い、戻り売り、バリュエーション調整、資金集中等）を表示。手動再解析ボタン対応 |
| 銘柄一覧・検索 | [10,477銘柄](https://trade-information.laravel.cloud/Meigara)（日本株・米国株・日米ETF・世界主要市場）を企業名・日本語名・英語別名・証券コード（ティッカー）からインクリメンタル検索（`/` キーショートカット、リアルタイムサジェスト、キーボード上下移動対応、市場横断ヒット件数表示）。38市場（アジア12・南北アメリカ6・欧州14・オセアニア2・中東3・アフリカ1）の国別フィルタ、テーマ別（高配当、メガバンク、商社、半導体、自動車、通信、米国テック、米国ETF）クイック絞り込み |
| 終値・騰落チェック & パルスボード | その日の取引が終わったときの終値と前日比騰落を表示（取得不可時は「終値なし」）。一覧ページごとの値動き集計（上昇・下落・変わらず銘柄数、平均騰落率、最大上昇・下落銘柄）。トップページに代表銘柄（トヨタ自動車、ソニーグループ、Apple、Microsoft）の終値と値動きパルスボード（上昇/下落/変わらず数、平均騰落率、一番上がった銘柄、一番下がった銘柄、ヒートマップタイル）を表示 |
| 全銘柄の株価・配当・割安度プレビュー | 代表銘柄（トヨタ 7203、三菱UFJ 8306、NTT 9432、Apple AAPL、Microsoft MSFT）をはじめ、登録されている全銘柄（`/try/{symbol}`）についてログイン不要で終値、日足推移グラフ（約4か月間の日足終値折れ線チャート）、配当利回り、1株あたり配当、PER、PBR、期間高値・安値、100株（1単元）買付時の必要資金・年間配当目安（税引前・月あたり目安）、過去配当推移（年ごとの実績一覧）、マクロ感応度診断プレビューを確認可能 |
| [100種類の分析計算ツール](https://trade-information.laravel.cloud/tools) | 登録・ログイン不要で利用可能。新NISA・成長投資枠で個別株を探す人向けの基本4ツール（配当利回り、割安度チェック（PER）、1年と1か月の配当、買うのに必要な金額）をはじめ、割安性・収益と安全性・損益と利回り・配当・資金とリスク・分割と為替の6カテゴリ・全100種類の計算ツールを公開 |
| [市場取引ルール・NISA解説](https://trade-information.laravel.cloud/Tradingrules) | 登録・ログイン不要で閲覧可能。初心者や新NISA向けに、今夜の市場状況（日本株・米国株の現在ステータス、受渡日目安、今年のNISA残り日数）、日本株（前場・後場・大引け・単元株・T+2受渡）と米国株（冬時間/夏時間・現地T+1受渡・2026年12月開始予定の平日23時間取引）の取引時間、新NISA（つみたて投資枠・成長投資枠・株式数比例配分方式・外国税額）、FXの基本と取引時間、日米の銘柄コード体系（英文字入り4桁コード・先頭2桁の業種目安）を整理 |
| 表示カスタマイズ・サイトマップ・SEO | 昼（ライト）と夜（ダーク）のテーマ切替。投資家モード（初心者・NISA・中級者・上級者）の選択および3問の診断質問（ヒアリング）。PC向けデスク帯・モバイル向けボトムドックバーに対応したレスポンシブ設計。訪問者向け[サイトマップ](https://trade-information.laravel.cloud/sitemap)および検索エンジン向け XML サイトマップ（`/sitemap.xml`）、全サブページ共通パンくずリスト、JSON-LD構造化データ、よくある質問（FAQ）を完備 |
| 投げ銭（開発支援）・規約・情報開示 | サイト維持・相場データ取得APIを支える任意の[投げ銭（開発支援）](https://trade-information.laravel.cloud/tip)（PAY.JP 決済：1回 100円〜100,000円の都度決済、500円/1,000円/3,000円/5,000円プリセットまたは自由入力、VISA / Mastercard / JCB / American Express / Diners Club / Discover / Apple Pay 対応、EMV 3-Dセキュア2.0本人認証、PCI DSS v4.0準拠・カード情報非保持化）と応援メッセージを掲載できるサポーターボード。[利用規約](https://trade-information.laravel.cloud/terms)、[プライバシーポリシー](https://trade-information.laravel.cloud/privacypolicy)、[免責事項](https://trade-information.laravel.cloud/disclaimer)、[特定商取引法に基づく表記](https://trade-information.laravel.cloud/tokushoho)、お問い合わせフォーム完備 |

### 会員機能（無料登録・要ログイン）

会員登録は無料です。パスワードは使わず、メールのログインリンク（マジックリンク）、パスキー（WebAuthn / FIDO2 生体認証）、または Google アカウントでログインできます。PCI DSS v4.0 およびクレジットカード不正利用防止対策ガイドラインに準拠した多層防御（不審IP遮断・クレジットマスター防御、2FA本人確認、本人確認情報管理・使い捨てメール排除、連続失敗時のアカウント/IP自動ロック、新規端末ログイン通知メール、属性・行動リスクスコア分析、SHA-256デバイスフィンガープリント検知）を実装しています。

| 機能 | 仕様・できること |
| --- | --- |
| 経済指標連動分析 | 米国・日本の主要マクロ経済指標（米10年債利回り、日米10年金利差、FFレート、日銀政策金利、CPI、雇用統計、短観DI等）の最新動向と推移。ドル円・日経平均・S&P500との相関・感応度マトリクス（ピアソン相関係数）、個別銘柄・為替の3大マクロ感応度診断（金利・為替・インフレ耐性スコア）、マクロシナリオ別セクター影響度、経済指標発表カレンダー・ライブパルス、先行シグナル、ポートフォリオストレステスト、イベントスタディ、マクロレジーム4象限分析、多変量マクロファクター重回帰分析、マクロ戦略バックテスト、マクロスクリーナー、カスタムマクロスプレッド計算機、モンテカルロ将来予測シミュレーター、ブラック・リッターマン最適資産配分、マクロショック・インパルス応答分析、イールドカーブPCA、個別銘柄のマクロ理論適正株価モデルを搭載 |
| 銘柄の詳細・インライン分析 | 全10,477銘柄の個別日足グラフ、テクニカル・ファンダメンタルズ・需給指標を詳細確認。チャート下部に株価や保有情報と自動連動するインライン分析ツール（目標株価・リスクリワード計算、許容損失から逆算する適正ポジションサイズ、手取り受取配当シミュレーション、バリュエーション理論株価診断、銘柄メモ）を搭載 |
| 為替（FX）マーケット | 円との交換レート推移。26通貨ペアの終値、前日比変動率、スパークライン、トレンド指標（SMA, EMA, ボリンジャーバンド, 一目均衡表, DMI/ADX, パラボリックSAR, エンベロープ）およびオシレーター指標（RSI, MACD, ストキャスティクス, サイコロジカルライン, RCI, 移動平均乖離率, ヒストリカル・ボラティリティ）による詳細分析 |
| ウォッチリスト | 気になる銘柄を登録・管理。カスタムタグ付け、目標株価・損切りラインの記録、「今夜の確認（Tonight）」フラグによる日々のチェック、CSVエクスポート、ウォッチリストから銘柄比較へのワンクリック連携 |
| ポートフォリオ（保有記録） | 保有銘柄の株数・取得単価・現在価格・タグを記録し、評価損益や取得金額割合を自動計算・可視化。CSVインポート／エクスポートに対応 |
| 投資メモ | 銘柄ごとに購入理由、目標価格・見直し価格、決算や取引の気付きを保存 |
| 銘柄比較 | 最大4銘柄の株価・騰落・配当利回り・PER・PBR・テクニカル指標などを横並びで比較。比較セットの保存・呼び出しに対応 |
| 資金計画シミュレーター | 投資資金と買付希望価格・許容リスクから買付可能株数や必要金額を自動計算し、ウォッチリストへ直接登録可能（売買推奨ではなく試算） |
| マイページ・データ管理 | 今夜チェックした銘柄の確認状況、手元の記録（ウォッチ・保有・メモ）のサマリー表示（メイプルによる要約）、本人確認ステータス・パスキー・登録済み端末フィンガープリントの確認、登録データの一括エクスポート（バックアップ）。管理者アカウントには会員管理・支援金履歴・セキュリティ監視（ClamAVマルウェア検査・不正IP/クレジットマスター遮断解除）・全体告知・銘柄一括管理を統合したシステム管理者コントロールパネルを表示 |

株価は1日に1回更新します。日本株は平日の夕方（取引終了後）に反映され、取引の途中の気配は含みません。この1日分を、日足と呼びます。日本株以外の株価と、通貨の交換レートも、その日の終わりの値段（終値）です。板情報や分足は出していません。このサイトは、1日の終わりの値段を見る場所です。投資助言や、売買の勧誘は行いません。

投げ銭（サイト運営支援）は任意（1回ごとの都度決済・100円〜100,000円）で、会員機能や投資助言の対価ではありません。自動更新や定期課金は発生せず、支援の有無や金額によって使える機能は変わりません。使途は相場データ取得APIおよびサーバー維持費です。公開を選択した場合はサイト内のサポーターボードへニックネームと応援メッセージが反映されます。[特定商取引法に基づく表記](https://trade-information.laravel.cloud/tokushoho)を置いています。

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
| 公開サイト | Laravel 13、PHP 8.5、MySQL、Alpine.js、Tailwind CSS。データ取得に J-Quants API / Financial Modeling Prep / Open Exchange Rates。パスワードレス認証（メールリンク、WebAuthn パスキー、Google OAuth）および PCI DSS v4.0 準拠の多層セキュリティ（デバイスフィンガープリント、属性・行動リスク分析、ClamAV連携）。PAY.JP（3Dセキュア2.0・トークン決済）による投げ銭決済、Google AdSense 広告配信 |
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
| 2026 | [trade-information](https://trade-information.laravel.cloud/) を Laravel 13（PHP 8.5）でリリース。画面の題は投資分析、ロゴの横は夜5分。夜5分、1日1回の株式チェック。世界マーケット相場（日米主要指数・為替・金利・コモディティのリアルタイム連動相場ボード、グリッド/ヒートマップ切替）・世界情勢ニュース＆トレード分析レーダー（マクロ地合いセンチメントゲージ、トレード戦略、影響指標バッジ）を搭載。10,477銘柄の検索・38市場国別フィルタ・テーマ別絞り込み、全銘柄の株価・配当・割安度プレビュー、市場取引ルール・NISA解説、分析計算ツール100種をログイン不要で一般公開。個別日足チャート＆インライン分析ツール・経済指標連動分析ダッシュボード・FX26通貨ペア・ウォッチ・保有・メモ・比較・資金計画は無料会員機能（メールリンク・パスキー・Googleによるパスワードレス認証、PCI DSS v4.0準拠の多層防御）。すべての基本機能を無料で提供し、Google AdSense および PAY.JP 投げ銭（サポーターボード）で運営 |

<div align="center">

<img src="https://raw.githubusercontent.com/key-pro/key-pro/output/github-contribution-grid-snake-dark.svg" alt="コントリビューションをなぞるスネーク" width="100%">

<img src="https://github-readme-stats.vercel.app/api?username=key-pro&show_icons=true&include_all_commits=true&locale=ja&hide_border=true&bg_color=060a12&title_color=67e8f9&icon_color=2dd4bf&text_color=e2e8f0" alt="GitHub stats" height="170">
<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=key-pro&layout=compact&locale=ja&hide_border=true&langs_count=6&bg_color=060a12&title_color=67e8f9&text_color=e2e8f0" alt="Top languages" height="170">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:060a12,100:22d3ee&height=80&section=footer&fontSize=1&text=&desc=" alt="" width="100%">

</div>
