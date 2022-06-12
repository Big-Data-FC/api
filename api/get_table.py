def get_table(appdb, league, season, compact=False) -> dict:
    """
    Returns the final table for the given {league} in season {season}
    """
    resp = appdb.get_table(league, season, compact)
    return resp.to_dict(orient="records")
