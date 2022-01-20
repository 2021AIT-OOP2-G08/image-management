from pymongo import MongoClient
from flask import Flask, request, render_template
import csv
from werkzeug.utils import secure_filename

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
def up():
    
    #データの登録処理
    prefecture_name = request.form.get("prefecture",None)
    image_pass = request.form.get("name",None)
    detail = request.form.get("detail",None)

    with open('image.csv') as f:
        csv_data = csv.reader(f)
        add_data = {"prefecture" : prefecture_name , "image" : image_pass , "detail" : detail}
        data = []
        for i in csv_data:
            data.append(i)
        data.append(add_data)
    
    with open('image.csv',"w") as f:
        writer = csv.writer(f)
        writer.writerows(data)

    if 'file' not in request.files:
        return render_template("upload.html", message="ファイルを指定してください。")

    #画像ファイルの受け取り
    fs = request.files['file']

    if '' == fs.filename:
        return render_template("upload.html", message="ファイルを指定してください。")

    #画像を保存
    fs.save('static/images/' + secure_filename(fs.filename))
    return render_template('upload.html', message='アップロードに成功しました。')
  
#画像表示、画像リスト表示
@app.route('/view', methods=["GET"])
def show_imagelist():
    #urlパラメータの取得
    prefecture_id = request.args.get('pref',None)
    #データベースの接続
    client = MongoClient('localhost', 27017)
    db = client.oop2
    #渡すデータの取得
    prefecture = db.prefectures.find_one({'id':prefecture_id})['ja']
    data = list(db.imgs.find({'prefecture':prefecture_id}))
    # 閉じる
    client.close()

    return render_template('imagelist.html',prefecture = prefecture,data = data)
    
if __name__ == "__main__":
    # debugモードが不要の場合は、debug=Trueを消してください
    app.run(debug=True)
