# request フォームから送信した情報を扱うためのモジュール
from flask import Flask, render_template, request, redirect, url_for

# アップロードされる拡張子の制限
ALLOWED_EXTENSIONS = set(['png'])


app = Flask(__name__)
"""
@app.route('/', methods=['GET', 'POST'])
#アップロード
def Home():
    if request.method == 'POST':
        img_file = request.files['img_file']
    return render_template('Home.html')
"""

@app.route('/')
#ホーム画面
def Eturan():
    return render_template('map.html')

#画像一覧ページに遷移
@app.route('/Image', methods=["POST"])
def Grayscale():
    return render_template('Image.html')

#アップロード画面に遷移
@app.route('/upload', methods=["POST"])
def Rinkaku():
    return render_template('upload.html')