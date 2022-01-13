from os import read
from flask import Flask, request, render_template

app = Flask(__name__)
@app.route('/', methods=["POST"])
def Home():
    return render_template('map.html')

# http://127.0.0.1:5000/address
@app.route('/upload', methods=["GET"])
def up():
    return render_template('upload.html')
    #データの登録処理
    image_name = request.form.get("im",None)
    image_pass = request.form.get("imp",None)

# http://127.0.0.1:5000/
@app.route('/view')
def image():
    return render_template('imagelist.html')


if __name__ == "__main__":
    # debugモードが不要の場合は、debug=Trueを消してください
    app.run(debug=True)