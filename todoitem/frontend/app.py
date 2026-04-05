from flask import Flask, render_template, request
import requests

BACKEND_URL = 'http://127.0.0.1:5001'
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/submittodoitem', methods=['POST'])
def submittodoitem():
    item_data = {
        "itemName": request.form.get("itemName"),
        "itemDescription": request.form.get("itemDescription")
    }
    print(item_data)  # debug
    
    requests.post(BACKEND_URL + '/submittodoitem', json=item_data,
    headers={"Content-Type": "application/json"} )
    
    return 'Data submitted successfully'

if __name__ == "__main__":
    app.run(debug=True, port=5000)