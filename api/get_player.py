def get_player(appdb, name, season) -> dict:
    """
    Returns player data with the given {name} and for
    the given {season}
    """
    resp = appdb.get_player_by_name(name, season)
    return resp.to_dict(orient="records")
