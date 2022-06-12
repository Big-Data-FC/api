def get_team(appdb, name, season) -> dict:
    """
    Returns team data with the given {name} and for
    the given {season}
    """
    team = appdb.get_team_by_name(name, season).to_dict(orient="records")
    players = appdb.get_players_in_team(name, season).to_dict(orient="records")
    return {"team_features": team, "players": players}
