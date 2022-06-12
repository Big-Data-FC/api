import pandas as pd


class Database:
    """
    Main database class
    """

    def __init__(self):
        print("Loading players dataset")
        self.players = pd.read_csv("data/players.csv")
        print("Columns: " + self.players.columns)

        print("Loading teams dataset")
        self.teams = pd.read_csv("data/teams.csv")
        print("Columns: " + self.teams.columns)

    def get_player_by_name(self, name, season):
        """
        Returns a Pandas dataframe object containing
        the player characterized by the given {name} and {season}
        """
        return self.players.loc[
            (self.players["short_name"] == name) & (self.players["season"] == season)
        ]

    def get_players_in_team(self, name, season):
        """
        Returns a Pandas dataframe object containing
        the players that played with {team} in {season}
        """
        return self.players.loc[
            (self.players["club_name"] == name) & (self.players["season"] == season)
        ]

    def get_team_by_name(self, name, season):
        """
        Returns a Pandas dataframe object containing
        the team characterized by the given {name} and {season}
        """
        return self.teams.loc[
            (self.teams["club_name"] == name) & (self.teams["year"] == season)
        ]
