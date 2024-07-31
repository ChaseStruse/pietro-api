import datetime

from src.services.player_service import calculate_player_gear_score, create_player_gear_entry


def test_calculate_player_gear_score_returns_correct_gear_score():
    expected = 200
    actual = calculate_player_gear_score(100, 100, 100)
    assert actual == expected


def test_create_player_gear_entry_returns_correct_given_valid_values():
    request_values = {
        "familyName": "Test",
        "ap": 100,
        "aap": 150,
        "dp": 200,
    }
    expected = {
        "family_name": "Test",
        "ap": 100,
        "aap": 150,
        "dp": 200,
        'gear_score': 325,
        "create_date": datetime.date.today(),
        "is_success": True
    }

    actual = create_player_gear_entry(request_values=request_values)
    assert actual == expected
