from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
CORS(app)

client = MongoClient(os.getenv("MONGO_URI"))
db = client[os.getenv("DB_NAME")]
collection = db["todos"]

@app.route("/submittodoitem", methods=["POST"])
def submit_todo_item():
    data = request.get_json()

    item_name = data.get("itemName")
    item_description = data.get("itemDescription")

    if not item_name:
        return jsonify({"message": "itemName is required"}), 400

    collection.insert_one({
        "itemName": item_name,
        "itemDescription": item_description
    })

    return jsonify({"message": "Item saved successfully!"}), 201

if __name__ == "__main__":
    app.run(debug=True, port=5001)