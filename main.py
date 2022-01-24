from cv2 import add
from flask import Flask, request, render_template
import csv
from werkzeug.utils import secure_filename
from pymongo import MongoClient
from db import DB
from nanoid import generate
import os

app = Flask(__name__)

#日本地図
@app.route('/')
def Home():
    return render_template('map.html')

#アップロード画面
@app.route('/upload', methods=["GET"])
def up_init():
    return render_template('upload.html')

#　都道府県名を取得したい場合
#  変数名 = request.args.get("pref", None)

#画像アップロード、csv書き込み
@app.route('/upload', methods=["POST"])
def upload():
    #画像ファイルの受け取り
    fs = request.files['file']
    if '' == fs.filename:
        return render_template("upload.html", message="ファイルを指定してください。")
    path, extension = os.path.splitext(fs.filename)
    filename = generate(size=10)+extension
    #画像を保存
    fs.save('static/images/' + filename)
    item = {
        'prefecture': request.form.get("prefecture",""),
        'name': request.form.get("name",""),
        'detail': request.form.get("detail",""),
        'path' : "static/images/" + filename
    }
    db = DB()
    db.add_one(item)
    return render_template('upload.html', message='アップロードに成功しました。')

    
#画像表示、画像リスト表示
@app.route('/view', methods=["GET"])
def show_imagelist():
    #urlパラメータの取得
    prefecture_id = request.args.get('pref',None)
    #データベースの接続
    db = DB()
    #渡すデータの取得
    data = db.get_filteredCollection('imgs',{'prefecture':prefecture_id})
    prefecture = db.get_document_one('prefectures',{'id':prefecture_id})

    return render_template('imagelist.html',prefecture = prefecture['ja'] ,data = data)
    
if __name__ == "__main__":
    # debugモードが不要の場合は、debug=Trueを消してください
    app.run(debug=True)
