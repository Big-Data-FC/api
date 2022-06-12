def get_prediction(appdb, league, season) -> dict:
    """
    Returns predicted table for the given {league} and {season}
    """
    return appdb.get_prediction(league, season).to_dict(orient="records")
