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
        'prefecture': request.form.get("prefecture",None),
        'name': request.form.get("name",None),
        'detail': request.form.get("detail",None),
        'path' : "static/images/" + filename
    }
    db = DB()
    db.add_one(item)
    return render_template('upload.html', message='アップロードに成功しました。')

    
#画像表示、画像リスト表示
@app.route('/view', methods=["GET"])
def image():
    #都道府県名を取得
    pref = request.args.get("pref",None)
    #csvから該当の都道府県名を含むデータを取得
    data = []
    with open('image.csv') as f:
        reader = csv.DictReader(f)
        for r in reader:
            if(r['prefecture'] == pref):
                data.append(r)
    return render_template('imagelist.html',prefecture = pref,data = data)
    

if __name__ == "__main__":
    # debugモードが不要の場合は、debug=Trueを消してください
    app.run(debug=True)
