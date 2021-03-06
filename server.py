import requests
import json

from flask import Flask
from flask import request
from flask import abort
from flask import jsonify

app = Flask("ReactDigitsServer", static_url_path="", static_folder="./")
app.add_url_rule("/", "root", lambda: app.send_static_file("index.html"))


@app.route("/user/verify", methods=["POST"])
def verify_user():
    data = json.loads(request.data)

    url = data["apiUrl"]
    auth = data["authHeader"]

    response = requests.get(url, headers={"Authorization": auth})

    if response.status_code != 200:
        return abort(response.status_code)

    return jsonify(json.loads(response.content))

app.run(debug=True)
