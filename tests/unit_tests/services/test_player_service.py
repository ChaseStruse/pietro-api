from src.services.player_service import calculate_player_gear_score


def test_calculate_player_gear_score_returns_correct_gear_score():
    expected = 200
    actual = calculate_player_gear_score(100, 100, 100)
    assert actual == expected

