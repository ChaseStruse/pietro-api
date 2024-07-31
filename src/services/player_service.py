def calculate_player_gear_score(ap: int, awakening_ap: int, dp: int) -> int:
    return int(((ap + awakening_ap) / 2) + dp)
