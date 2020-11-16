from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def home_page():
    return jsonify({
        "page": "homepage",
        "data": [1, 2, 3, 4]
    })
