#
# flaskr-skeletonの使い方
#

## 目標
WebフレームワークFlaskを使って簡易なWebアプリケーションのプロトタイプを"いつでも"つくって試せるように、
Flaskのスケルトンを作成しておく。


## ファイル
./
	/flaskr.py
	/schema.py
	/schema.sql
	/templates/
		/logout.html
		/login.html
		/show_entries.html
	/static/
		/style.css


## データベース
- データベースにはSqlite3を利用しています


## 機能
- メイン画面
show_entries.html
index.html
- ログイン/ログアウト機能
ログイン/ログアウトの機能を備えており、ログイン/アウトの状態により表示を変更できる。


## CSSフレームワーク
- CSSフレームワークにはBootstrapを導入しています
- 事前にflask-bootstrapをインストールしておく必要があります。

	pip install flask-bootstrap

- Bootstrapの利用には"bootstrapbase.html"を継承して利用します。

## javascriptフレームワーク
- javascriptフレームワークにはjQueryを導入しています
- jqueryの呼び出し元は"flask-bootstrap"と一緒にインストールされています。
- jQueryの利用には"bootstrapbase.html"を継承して利用します。


## 初めての使い方

