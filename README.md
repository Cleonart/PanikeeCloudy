# PanikeeCloudy
Panikee Repository for Handling Cloud

#Documentation
This repository is mainly to handle all things that is going to be uploaded to GCP later. This includes API to locate emergency service location in "main.py", and
the requirements.txt file contains the programs needed to be installed before running the API.

#main.py

from flask import Flask, jsonify
from flask_cors import CORS
from model.EmergencyFacilityModel import model

app = Flask(__name__)
CORS(app)


@app.route("/facility/emergency")
def main():
    list = []
    list.append(model("Poltabes Manado", "081119291", "1.471427", "124.843633", "police"))
    list.append(model("Polsek Tikala", "0821111", "1.474717019997341", "124.87413355769698", "police"))
    return jsonify(list)

if __name__ == "__main__":
   app.run(debug=True, host="0.0.0.0")
   
#Explanation
Used to send the data listed to the model, which will be shown later in the website
