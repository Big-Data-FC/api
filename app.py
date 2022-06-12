#!python3

import json
from flask import Flask, request

import api
from db import Database

app = Flask(__name__)
db = Database()


@app.route("/player", methods=["GET"])
def get_player():
    """
    Get features of a player
    """
    data = json.loads(request.data)
    player = api.get_player(db, data["playerName"], data["season"])
    return player.to_json(orient="records")


if __name__ == "__main__":
    app.run(port=8080, debug=True)
