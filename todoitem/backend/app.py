from flask import Flask, request, jsonify
from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import os
from pymongo.server_api import ServerApi

load_dotenv()
MONGO_URI = os.getenv('MONGO_URI')

client = MongoClient(MONGO_URI, server_api=ServerApi('1'))
db = client.test
collection = db["todos"]
app = Flask(__name__)

@app.route("/submittodoitem", methods=["GET", "POST"])

@app.route("/submittodoitem", methods=["GET", "POST"])
def submit_todo_item():

    if request.method == "POST":
        item_data = request.get_json()

        collection.insert_one({
            "itemName": item_data.get("itemName"),
            "itemDescription": item_data.get("itemDescription")
        })

        return jsonify({"message": "Saved successfully"}), 201

    if request.method == "GET":
        data = list(collection.find({}, {"_id": 0}))
        return jsonify(data)

if __name__ == "__main__":

    app.run(host='0.0.0.0', port=5001, debug=True)