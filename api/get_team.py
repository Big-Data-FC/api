def get_team(appdb, name, season) -> dict:
    """
    Returns team data with the given {name} and for
    the given {season}
    """
    resp = appdb.get_team_by_name(name, season)
    return resp
