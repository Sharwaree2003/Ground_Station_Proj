from flask import Flask, jsonify
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

client = MongoClient("mongodb://localhost:27017/")
db = client["ground_station"]

@app.route("/")
def home():
    return jsonify({"status": "Backend + MongoDB running"})

@app.route("/api/test")
def test_db():
    db.test.insert_one({"msg": "hello"})
    return jsonify({"db": "write success"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

