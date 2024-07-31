import json
from src.services.player_service import calculate_player_gear_score, create_player_gear_entry
from flask import jsonify, request
from src.controllers import app


@app.route('/player/gearscore', methods=['POST'])
def get_player_gear_score():
    values = json.loads(request.data)
    gear_score = calculate_player_gear_score(ap=int(values["ap"]), awakening_ap=int(values["aap"]),
                                             dp=int(values["dp"]))
    return jsonify({"gearScore": gear_score}), 200


@app.route('/player/gearentry', methods=['POST'])
def post_player_gear_entry():
    values = json.loads(request.data)
    result = create_player_gear_entry(values)
    return jsonify(result), 200


if __name__ == '__main__':
    app.run(port=5000)
