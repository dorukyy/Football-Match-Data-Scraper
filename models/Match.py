from sqlalchemy import Column, Integer, String
from base import Base

# Match class is used to create a match object and store it in the database
class Match(Base):
    __tablename__ = 'matches'

    id = Column(Integer, primary_key=True)  # Auto incrementing ID
    date = Column(String)  # Date of the match
    time = Column(String)  # Time of the match
    league = Column(String)  # League of the match
    tour = Column(String)  # Tour of the match
    home_team = Column(String)  # Home team of the match
    second_half = Column(String)  # Second half score of the match
    away_team = Column(String)  # Away team of the match
    first_half = Column(String)  # First half score of the match
    odds_1 = Column(Integer)  # Odds of home team win
    odds_x = Column(Integer)  # Odds of draw
    odds_2 = Column(Integer)  # Odds of away team win
    under = Column(String)  # Odds of under 2.5 goals
    over = Column(String)  # Odds of over 2.5 goals
    both_teams_score = Column(String)  # Odds of both teams score
    no_goal = Column(String)  # Odds of no goal
    first_half_home_team_goals = Column(Integer)  # Home team goals in first half
    first_half_away_team_goals = Column(Integer)  # Away team goals in first half
    second_half_home_team_goals = Column(Integer)  # Home team goals in second half
    second_half_away_team_goals = Column(Integer)  # Away team goals in second half
    first_half_winner = Column(Integer)  # Winner of first half
    full_time_winner = Column(Integer)  # Winner of full time
    bet_index = Column(Integer)  # Index of the bet (1,2,3 1 for the lowes odd, 3 for the highest odd)

    def __init__(self, data):
        self.date = data.get("date")
        self.time = data.get("time")
        self.league = data.get("league")
        self.tour = data.get("tour")
        self.home_team = data.get("home_team")
        self.second_half = data.get("second_half")
        self.away_team = data.get("away_team")
        self.first_half = data.get("first_half")
        self.odds_1 = data.get("odds_1")
        self.odds_x = data.get("odds_x")
        self.odds_2 = data.get("odds_2")
        self.under = data.get("under")
        self.over = data.get("over")
        self.both_teams_score = data.get("both_teams_score")
        self.no_goal = data.get("no_goal")
        self.first_half_home_team_goals = int(data.get("first_half").split("-")[0])
        self.first_half_away_team_goals = int(data.get("first_half").split("-")[1])
        self.second_half_home_team_goals = int(data.get("second_half").split("-")[0])
        self.second_half_away_team_goals = int(data.get("second_half").split("-")[1])
        self.first_half_winner = self.get_winner(data.get("first_half"))
        self.full_time_winner = self.get_winner(data.get("second_half"))
        self.bet_index = self.set_bet_index()

    def get_winner(self, score):
        home_goals, away_goals = map(int, score.split("-"))
        if home_goals == away_goals:
            return 0
        elif home_goals > away_goals:
            return 1
        else:
            return 2

    # This method is used to set the bet index of the match object based on the odds of the match
    def set_bet_index(self):
        if self.odds_1 is None or self.odds_x is None or self.odds_2 is None:
            bet_index = None
        else:
            data_map = {
                '1': self.odds_1,
                '0': self.odds_x,
                '2': self.odds_2,
            }
            data_map = dict(sorted(data_map.items(), key=lambda item: float(item[1])))
            bet_index = (list(data_map.keys()).index(str(self.full_time_winner))) + 1

        return bet_index
