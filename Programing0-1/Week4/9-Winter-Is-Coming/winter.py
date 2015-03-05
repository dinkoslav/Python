def winter_is_coming(seasons):
    season_types = ["winter", "summer", "spring"]
    season_count = 0
    for season in seasons:
        if season in season_types:
            if season == season_types[0]:
                season_count = 0
            else:
                season_count = season_count + 1
    if season_count == 5:
        return True
    else:
        return False

seasons = ["winter", "summer", "summer", "summer", "spring", "spring"]
is_winter = winter_is_coming(seasons)
print(is_winter)
