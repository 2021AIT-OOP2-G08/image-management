from os import read
from flask import Flask, request, render_template
import csv

app = Flask(__name__)

#日本地図
@app.route('/')
def Home():
    return render_template('map.html')

#画像アップロード、csv書き込み
@app.route('/upload', methods=["GET"])
def up():
    return render_template('upload.html')
    #データの登録処理
    image_name = request.form.get("im",None)
    image_pass = request.form.get("imp",None)

#画像表示、画像リスト表示
@app.route('/view')
def image():
    

    return render_template('imagelist.html')


if __name__ == "__main__":
    # debugモードが不要の場合は、debug=Trueを消してください
    app.run(debug=True)