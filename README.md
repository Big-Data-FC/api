# Big Data FC - REST API

This repository contains the code for the API built for the Big Data FC project.

## Running

To run the project it is sufficient to:

1. Install requirements with `pip3 install -r requirements.txt`.
2. Run the API with `flask run`.

The API will listen on port `5000`.

Alternatively, the API can also be run by executing `./app.py`.

## Needed data

The API allows getting team features, player features, league tables and predictions, hence the needed data is:

* Player features, in a single CSV file in `./data/players.csv`.
* Team features, in a single CSV file in `./data/teams.csv`.
* Predictions dataframe, in a pickle directory in `./data/df.pkl`.
* PySpark Learning model, exported in `./data/model`.

Said CSV files can be exported from the dataframes in the main project. A sample of them is already provided in this repository.

Dataframe pickle and learning model can also be exported from the main repository. As a sample, this project currently uses the Linear Regression model.

## API specification

The following use-cases can informally be defined:

* `GetPlayer(playerName, year)` → `{}playerFeatures`
* `GetTeam(teamName, year)` → `{ {}teamFeatures, {}players }`
* `GetTable(league, year)` → `{}table`
* `Predict(league, year)` → `{}table`

### Endpoints

#### `GET /player`

Gets the features of the given player for a specific season.

Example body:

```json
{
  "playerName": "L. Messi",
  "season": 19
}
```

Example response:

```json
[
    {
        "attacking_crossing": 88,
        "attacking_finishing": 95,
        "attacking_heading_accuracy": 70,
        "attacking_short_passing": 92,
        "club_name": "FC Barcelona",
        "defending": 39,
        "defending_standing_tackle": 37,
        "dribbling": 96,
        "league_name": "Spain Primera Division",
        "mentality_aggression": 48,
        "mentality_penalties": 75,
        "movement_acceleration": 91,
        "movement_reactions": 95,
        "movement_sprint_speed": 84,
        "pace": 87,
        "passing": 92,
        "physic": 66,
        "player_positions": "RW, CF, ST",
        "power_long_shots": 94,
        "power_shot_power": 86,
        "power_stamina": 75,
        "power_strength": 68,
        "season": 19,
        "shooting": 92,
        "short_name": "L. Messi",
        "skill_ball_control": 96,
        "skill_dribbling": 97,
        "skill_fk_accuracy": 94,
        "skill_long_passing": 92
    }
]
```

#### `GET /team`

Gets the team information for a specific season, along with its players.

If `"compact": true`, then a list of player names will be returned instead of the complete players features.

Example body:

```json
{
  "teamName": "Roma",
  "season": 15,
  "compact": true
}
```

Example response:

```json
{
    "players": [
        "Gervinho",
        "K. Manolas",
        "L. Digne",
        "A. Florenzi",
        "M. Salah",
        "N. Gyömbér",
        "S. Anočič",
        "F. Totti",
        "Maicon",
        "R. Nainggolan",
        "V. Torosidis",
        "K. Strootman",
        "E. Capradossi",
        "S. Uçan",
        "A. Cole",
        "M. Pjanić",
        "A. Rüdiger",
        "José Machín",
        "D. De Rossi",
        "S. Keita",
        "Leandro Castán",
        "E. Džeko",
        "Iago Falqué",
        "J. Iturbe"
    ],
    "team_features": [
        {
            "avg(attacking_crossing)": 61.583333333333336,
            "avg(attacking_finishing)": 51.833333333333336,
            "avg(attacking_heading_accuracy)": 64.16666666666667,
            "avg(attacking_short_passing)": 71.91666666666667,
            "avg(defending)": 62.04166666666666,
            "avg(defending_standing_tackle)": 64.41666666666667,
            "avg(dribbling)": 70.04166666666667,
            "avg(mentality_aggression)": 71.54166666666667,
            "avg(mentality_penalties)": 56.125,
            "avg(movement_acceleration)": 73.20833333333333,
            "avg(movement_reactions)": 74.5,
            "avg(movement_sprint_speed)": 72.875,
            "avg(pace)": 73.0,
            "avg(passing)": 65.45833333333333,
            "avg(physic)": 70.375,
            "avg(power_long_shots)": 60.41666666666666,
            "avg(power_shot_power)": 69.75,
            "avg(power_stamina)": 73.25,
            "avg(power_strength)": 68.625,
            "avg(shooting)": 57.958333333333336,
            "avg(skill_ball_control)": 74.20833333333333,
            "avg(skill_dribbling)": 67.33333333333333,
            "avg(skill_fk_accuracy)": 52.625,
            "avg(skill_long_passing)": 67.375,
            "club_name": "Roma",
            "club_name_ext": "Roma",
            "league": "Italian Serie A",
            "place": 3,
            "points": 80.0,
            "season": 15,
            "year": 15
        }
    ]
}
```

#### `GET /table`

Get the final table for a specific league in a specific season.

If `"compact": true`, then team's features are not returned.

Example body:

```json
{
  "league": "Italian Serie A",
  "season": 19,
  "compact": true
}
```

Example response:

```json
[
    {
        "club_name_ext": "Juventus",
        "place": 1,
        "points": 83.0
    },
    {
        "club_name_ext": "Inter",
        "place": 2,
        "points": 82.0
    },
    {
        "club_name_ext": "Atalanta",
        "place": 3,
        "points": 78.0
    },
    {
        "club_name_ext": "Lazio",
        "place": 4,
        "points": 78.0
    },
    {
        "club_name_ext": "Roma",
        "place": 5,
        "points": 70.0
    },
    {
        "club_name_ext": "Milan",
        "place": 6,
        "points": 66.0
    },
    {
        "club_name_ext": "Napoli",
        "place": 7,
        "points": 62.0
    },
    {
        "club_name_ext": "Sassuolo",
        "place": 8,
        "points": 51.0
    },
    {
        "club_name_ext": "Hellas Verona",
        "place": 9,
        "points": 49.0
    },
    {
        "club_name_ext": "Fiorentina",
        "place": 10,
        "points": 49.0
    },
    {
        "club_name_ext": "Parma",
        "place": 11,
        "points": 49.0
    },
    {
        "club_name_ext": "Bologna",
        "place": 12,
        "points": 47.0
    },
    {
        "club_name_ext": "Udinese",
        "place": 13,
        "points": 45.0
    },
    {
        "club_name_ext": "Cagliari",
        "place": 14,
        "points": 45.0
    },
    {
        "club_name_ext": "Sampdoria",
        "place": 15,
        "points": 42.0
    },
    {
        "club_name_ext": "Torino",
        "place": 16,
        "points": 40.0
    },
    {
        "club_name_ext": "Genoa",
        "place": 17,
        "points": 39.0
    },
    {
        "club_name_ext": "Lecce",
        "place": 18,
        "points": 35.0
    },
    {
        "club_name_ext": "Brescia",
        "place": 19,
        "points": 25.0
    },
    {
        "club_name_ext": "SPAL",
        "place": 20,
        "points": 20.0
    }
]
```

#### `GET /predict`

Get predictions for a specific league and season.

Example body:

```json
{
  "league": "Italian Serie A",
  "season": 20
}
```

Example response:

```json
[
    {
        "club_name": "Juventus",
        "league": "Italian Serie A",
        "points": 78.0,
        "prediction": 73.41170178534836,
        "season": "20"
    },
    {
        "club_name": "Inter",
        "league": "Italian Serie A",
        "points": 91.0,
        "prediction": 72.40765187271296,
        "season": "20"
    },
    {
        "club_name": "Napoli",
        "league": "Italian Serie A",
        "points": 77.0,
        "prediction": 69.16208198417701,
        "season": "20"
    },
    {
        "club_name": "Lazio",
        "league": "Italian Serie A",
        "points": 68.0,
        "prediction": 64.21875497063937,
        "season": "20"
    },
    {
        "club_name": "Roma",
        "league": "Italian Serie A",
        "points": 62.0,
        "prediction": 63.53082085023385,
        "season": "20"
    },
    {
        "club_name": "Milan",
        "league": "Italian Serie A",
        "points": 79.0,
        "prediction": 62.814598579220586,
        "season": "20"
    },
    {
        "club_name": "Atalanta",
        "league": "Italian Serie A",
        "points": 78.0,
        "prediction": 57.78263510039619,
        "season": "20"
    },
    {
        "club_name": "Fiorentina",
        "league": "Italian Serie A",
        "points": 40.0,
        "prediction": 53.58237913622716,
        "season": "20"
    },
    {
        "club_name": "Sassuolo",
        "league": "Italian Serie A",
        "points": 62.0,
        "prediction": 50.1505880245785,
        "season": "20"
    },
    {
        "club_name": "Torino",
        "league": "Italian Serie A",
        "points": 37.0,
        "prediction": 50.07513215235619,
        "season": "20"
    },
    {
        "club_name": "Udinese",
        "league": "Italian Serie A",
        "points": 40.0,
        "prediction": 49.337986323723015,
        "season": "20"
    },
    {
        "club_name": "Parma",
        "league": "Italian Serie A",
        "points": 20.0,
        "prediction": 48.53700882154524,
        "season": "20"
    },
    {
        "club_name": "Genoa",
        "league": "Italian Serie A",
        "points": 42.0,
        "prediction": 48.210985155274585,
        "season": "20"
    },
    {
        "club_name": "Sampdoria",
        "league": "Italian Serie A",
        "points": 52.0,
        "prediction": 48.13371543997002,
        "season": "20"
    },
    {
        "club_name": "Bologna",
        "league": "Italian Serie A",
        "points": 41.0,
        "prediction": 45.497475904203526,
        "season": "20"
    },
    {
        "club_name": "Hellas Verona",
        "league": "Italian Serie A",
        "points": 45.0,
        "prediction": 44.94413284124002,
        "season": "20"
    },
    {
        "club_name": "Cagliari",
        "league": "Italian Serie A",
        "points": 37.0,
        "prediction": 44.81365706218898,
        "season": "20"
    },
    {
        "club_name": "Benevento",
        "league": "Italian Serie A",
        "points": 33.0,
        "prediction": 34.14765512409974,
        "season": "20"
    },
    {
        "club_name": "Crotone",
        "league": "Italian Serie A",
        "points": 23.0,
        "prediction": 30.767860847476044,
        "season": "20"
    },
    {
        "club_name": "Spezia",
        "league": "Italian Serie A",
        "points": 39.0,
        "prediction": 28.95803552515497,
        "season": "20"
    }
]
```

### Postman

The [Postman collection](api.postman_collection.json) can be used to quickly import sample requests to test the API.