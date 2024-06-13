
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

ultra = {
    "sensor":{
        "ultrasonik":{
            "value":0
        }
    }
}

@app.route('/sensor', methods=["POST","GET"])
def send_sensor():
    if request.method == "POST":
        tipe = request.form.get("type")
        if tipe == "ultrasonik":
            ultra["sensor"]["ultrasonik"]["value"] = int(request.form.get("value"))
        return jsonify(ultra)
    else:
        return jsonify(ultra)
    

@app.route('/', methods=["GET"])
def entry_point():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000)