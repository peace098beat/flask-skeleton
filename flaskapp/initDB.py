# -*- coding: utf-8 -*-
#
# データベースの初期化用プログラム
#
# 初期化が必要なタイミング
#	: アプリを初めて動かす時
#	: DBをリセットしたい時
#
# Example
#	$ python initDB.py
#


from flaskr import init_db

init_db()
