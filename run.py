from flask import Flask, render_template, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/get-data")
def get_data():
    return jsonify({"a": 1, "b": 2})


if __name__ == '__main__':
    app.debug = True
    app.run()
