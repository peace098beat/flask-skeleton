# -*- coding: utf-8 -*-
# db
import sqlite3
# default
from contextlib import closing
from flask import Flask, request, session, g, redirect
from flask import url_for, abort, render_template, flash
from flask import jsonify  # Ajax
# css
from flask_bootstrap import Bootstrap
# user module
from umod.user_module import *

#########################################################################
#
# 環境変数
#
#########################################################################

# 各種設定情報を記述
DATABASE = 'flaskr.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

#########################################################################
#
# アプリ生成
#
#########################################################################

app = Flask(__name__)
Bootstrap(app)
# from_object() では、与えられたオブジェクトの内で 大文字の変数をすべて取得します。大変便利ですね。
# 今回は flask.py ファイル自体を 渡していますが、コンフィグを別ファイルに書いた場合には、適宜書き換えてください。
app.config.from_object(__name__)
# @from_envvar 環境変数から設定を引き継ぐことも出来ます from_envvar()
app.config.from_envvar('FLASKR_SETTINGS', silent=True)


#########################################################################
#
# DB接続
#
#########################################################################
# DB接続
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


# DBの初期化
def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql') as f:
            db.cursor().executescript(f.read())
        db.commit()


#########################################################################
#
#　デコレータ
#
# flaskは、DB処理の前後で別処理をするには以下のようなデコレータを利用することで可能になります。
# before_request() もしくわ after_request()
#########################################################################

# リクエストに対する前処理
@app.before_request
def before_request():
    # リクエストがきたらまずDBへ接続する。
    g.db = connect_db()


# リクエストに対する後処理
@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()


#########################################################################
#
# View
#
#########################################################################
# index.htmlページ
@app.route('/')
def index():
    return render_template('index.html')


# aboutページ
@app.route('/about')
def about():
    return render_template('about.html')


# releaseページ
@app.route('/release')
def release():
    return render_template('release.html')


# releaseページ
@app.route('/css_design')
def css_design():
    return render_template('css_design.html')


# DBのエントリー一覧ページ
@app.route('/show_entris')
def show_entries():
    # DBからエントリを取得する
    cur = g.db.execute('select title, text from entries order by id desc')
    # 複数のエントリの整形
    entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    # 取得したエントリを使ってhtmlをレンダリング
    return render_template('index.html', entries=entries)


# エントリー追加
@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    g.db.execute('insert into entries (title, text) values (?, ?)',
                 [request.form['title'], request.form['text']])
    g.db.commit()
    flash(u'新しいエントリーが追加されました')
    return redirect(url_for('show_entries'))


# Ajaxを使って選択要素の情報を取得
# http://runnable.com/UiPhLHanceFYAAAP/how-to-perform-ajax-in-flask-for-python
@app.route('/_ajax_getJSON')
def ajax_getJSON():
    arg = request.args.get('a', 0, type=int)

    inc = arg + 1
    dec = arg - 1

    ret = dict(inc=inc, dec=dec)
    ret_json = jsonify(result=ret)

    return ret_json


#########################################################################
#
# LOGIN/LOGOUT
#
# ログインとログアウト
# 以下のファンクションは、ユーザーのログインとログアウト時に使います。
#########################################################################

# ログイン
# ログインには、ユーザーネームとパスワードを利用して行ない、session内に logged_in のキーで設定がセットされます。
# もし、ログイン済みの場合は、Keyは True がセットされている ので、ユーザは show_entries ページにリダイレクトされます。
# 追加メッセージで、ユーザに ログインが成功した事が通知され、もしエラーが発生した場合は、ユーザに再度入力を求める
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    # POSTのみ利用可能
    if request.method == 'POST':
        # ユーザネームの照合(照合先は先に設定した設定変数)
        if request.form['username'] != app.config['USERNAME']:
            error = u'ユーザ名が間違っています'
        # パスワードの照合(照合先は先に設定した設定変数)
        elif request.form['password'] != app.config['PASSWORD']:
            error = u'パスワードが間違っています'
        # 照合成功!
        else:
            # ログインセッションをTrueにする。これが鍵になる。
            session['logged_in'] = True
            flash(u'ログインしました')
            # ログインできたら
            return redirect(url_for('show_entries'))
    # ログイン失敗時に再度login.htmlへリダイレクトされる
    return render_template('login.html', error=error)


# ログアウト
# ログアウト処理は、sessionからkeyを削除します。
# また、以下のような方法でもログアウト処理を行えます。
# pop() を 使用することでsession内からkeyを削除することが出来ます。
# 未ログイン状態でも 以下のメソッドは使用可能なので、ログイン状態チェックすることなく利用する事が 可能です。
@app.route('/logout')
def logout():
    # pop() を 使用することでsession内からkeyを削除することが出来ます。
    session.pop('logged_in', None)
    flash(u'ログアウトしました')
    return redirect(url_for('show_entries'))


if __name__ == '__main__':
    user_module_demo()
    user_module_func()
    app.run(host='0.0.0.0', debug=True)
