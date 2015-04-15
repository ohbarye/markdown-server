# What is 'markdown-server' ?
MarkdownをHTML化して`text/html`形式でレスポンスするシンプルなWebアプリケーションです。

Markdown Engineは**Github Flavered Markdown**です。

## How to use

### Runtime Environment
python実行環境が必要です。

### Library Dependencies
下記ライブラリに依存しています。

|No.|Name|Description|
|:---|:---|:---|
|1|markdown|Markdown -> HTML 変換ライブラリ|
|2|pygments|シンタックスハイライト用|
|3|bottle|Webアプリケーションフレームワーク|
|4|codecs|ファイル読み書き用|

### Just try
試すだけであれば特別な準備は何も必要ありません。
下記コマンドを実行するだけでサーバが起動します。

```
$ python start_sarver.py
```

サーバが起動したら下記アドレスにアクセスし、サンプルMarkdownファイルの変換結果を確認してみてください。
```
$ open http://localhost:8009/sample.md
```

### Do as you like
* markdown-server は`resources/markdown`ディレクトリに配置されたファイルに対し、`http://host/[file_name]`の形式でルーティングを提供します。任意のファイルを置いてください。

* 変換されたファイルは`resources/html`ディレクトリに配置されます。HTMLファイルにCSSも組み込まれています。

* ホスト名やポート番号などの環境変数は`env.py`にまとめています。適宜変更してください。
```python
ms_port        = '8009'
ms_host        = 'localhost'
```

* デフォルトの Markdown Engine は**Github Flavered Markdown**です。好みに応じてCSSファイルを差し替え、`env.py`を編集してください。
```python
css_name       = 'github.css'
markdown_type  = 'gfm'
```
