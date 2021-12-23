# request フォームから送信した情報を扱うためのモジュール
from flask import Flask, render_template, request, redirect, url_for

# アップロードされる拡張子の制限
ALLOWED_EXTENSIONS = set(['png'])


app = Flask(__name__)

@app.route('/')
#ホーム画面
def map():
    return render_template('map.html')

#画像一覧ページに遷移
@app.route('/imagelist', methods=["POST"])
def imagelist():
    return render_template('imagelist.html')

#アップロード画面に遷移
@app.route('/upload', methods=["POST"])
def upload():
    return render_template('upload.html')

if __name__ == "__main__":
    # debugモードが不要の場合は、debug=Trueを消してください
    app.run(host="localhost", port=8888, debug=True)