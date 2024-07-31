import datetime
from src.repositories import player_repository as repository


def calculate_player_gear_score(ap: int, awakening_ap: int, dp: int) -> int:
    return int(((ap + awakening_ap) / 2) + dp)


def create_player_gear_entry(request_values: dict) -> dict:
    gear_entry = {
        "family_name": request_values["familyName"],
        "ap": request_values["ap"],
        "aap": request_values["aap"],
        "dp": request_values["dp"],
        "gear_score": calculate_player_gear_score(ap=int(request_values["ap"]),
                                                  awakening_ap=int(request_values["aap"]),
                                                  dp=int(request_values["dp"])),
        "create_date": datetime.date.today()
    }
    return repository.create_player_gear_entry(gear_entry)
