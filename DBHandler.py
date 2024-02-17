from base import Base
from models.Match import Match, Base
from models.Week import Week, Base
from future.moves import configparser
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBHandler:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        db_url = config.get('DEFAULT', 'db_url')
        self.engine = create_engine(db_url)
        self.Session = sessionmaker(bind=self.engine)

    # This method creates the tables in the database.
    def create_tables(self):
        Base.metadata.create_all(self.engine)
        print("Tables created successfully.")

    # This method lists the tables in the database.
    def list_tables(self):
        return Base.metadata.tables.keys()

    # This method adds a match to the database if it does not exist.
    def add_match(self, match):
        session = self.Session()
        if self.is_match_exists(match) is False:
            session.add(match)
            session.commit()
        session.close()

    # This method checks if a match exists in the database.
    def is_match_exists(self, match) -> bool:
        session = self.Session()
        existing_match = session.query(Match).filter_by(date=match.date, time=match.time, league=match.league,
                                                        home_team=match.home_team,
                                                        second_half=match.second_half,
                                                        away_team=match.away_team, first_half=match.first_half,
                                                        odds_1=match.odds_1, odds_x=match.odds_x, odds_2=match.odds_2,
                                                        ).first()
        session.close()
        return True if existing_match else False

    def add_matches(self, matches):
        session = self.Session()
        for match in matches:
            if not self.is_match_exists(match):
                session.add(match)
        session.commit()
        session.close()

    # This method gets a match by its match_id.
    def get_match_by_match_id(self, match_id):
        session = self.Session()
        match = session.query(Match).filter_by(id=match_id).first()
        session.close()
        return match

    # This method inserts a week to the database if it does not exist.
    def insert_week(self, start_date, end_date):
        session = self.Session()
        week = Week(start_date=start_date, end_date=end_date)
        if self.is_week_exists(start_date, end_date) is False:
            session.add(week)
            session.commit()
            session.close()
            return True
        else:
            session.close()
            return False

    # This method checks if a week exists in the database.
    def is_week_exists(self, start_date, end_date):
        session = self.Session()
        existing_week = session.query(Week).filter_by(start_date=start_date, end_date=end_date).first()
        session.close()
        return True if existing_week else False

    # This method gets all the matches in the database.
    def get_all_matches(self):
        session = self.Session()
        matches = session.query(Match).all()
        session.close()
        return matches
