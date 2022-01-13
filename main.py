from os import read
from flask import Flask, request, render_template
import csv

app = Flask(__name__)

#日本地図
@app.route('/')
def Home():
    return render_template('map.html')


#　都道府県名を取得したい場合
#  変数名 = request.args.get("pref", None)

#画像アップロード、csv書き込み
@app.route('/upload', methods=["GET"])
def up():
    return render_template('upload.html')
    #データの登録処理
    image_name = request.form.get("im",None)
    image_pass = request.form.get("imp",None)
    #画像のアップロード先のディレクトリ
    UPLOAD_FOLDER = './images'
    #アップロードされる拡張子の制限
    ALLOWED_EXTENSIONS = set([jpg])

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
