#!python3

import json
from flask import Flask, request, jsonify


import api
from db import Database
from spark import Spark

app = Flask(__name__)
spark = Spark()
db = Database(spark)


@app.route("/player", methods=["GET"])
def get_player():
    """
    Get features of a player
    """
    data = json.loads(request.data)
    player = api.get_player(db, data["playerName"], data["season"])
    return jsonify(player)


@app.route("/team", methods=["GET"])
def get_team():
    """
    Get features of a team
    """
    data = json.loads(request.data)
    team = api.get_team(
        db, data["teamName"], data["season"], __handle_compact_field(data)
    )
    return jsonify(team)


@app.route("/table", methods=["GET"])
def get_table():
    """
    Get the final league table
    """
    data = json.loads(request.data)
    table = api.get_table(
        db, data["league"], data["season"], __handle_compact_field(data)
    )
    return jsonify(table)


@app.route("/predict", methods=["GET"])
def predict_table():
    """
    Perform predictions
    """
    data = json.loads(request.data)
    prediction = api.get_prediction(db, data["league"], data["season"])

    return jsonify(prediction)


def __handle_compact_field(data) -> bool:
    return data["compact"] if "compact" in data.keys() else False


if __name__ == "__main__":
    app.run(port=8080, debug=True)
