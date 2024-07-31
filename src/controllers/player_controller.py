import json

from src.services.player_service import calculate_player_gear_score
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/player/gearscore', methods=['POST'])
def get_player_gear_score():
    values = json.loads(request.data)
    gear_score = calculate_player_gear_score(ap=int(values["ap"]), awakening_ap=int(values["aap"]),
                                             dp=int(values["dp"]))
    return jsonify({"gearScore": gear_score}), 200


if __name__ == '__main__':
    app.run(port=5000)
