import datetime


def create_player_gear_entry(gear_entry: dict):
    gear = {
        "family_name": gear_entry["family_name"],
        "ap": gear_entry["ap"],
        "aap": gear_entry["aap"],
        "dp": gear_entry["dp"],
        "gear_score": gear_entry["gear_score"],
        "create_date": datetime.date.today(),
        "is_success": True
    }
    return gear
