from DBHandler import DBHandler
from services.MatchScraper import MatchScraper


if __name__ == '__main__':
    db = DBHandler()
    db.create_tables()
    ms = MatchScraper()
    ms.open()
    ms.select_all_dates()
    date_range_values = ms.get_date_range_values()
    if date_range_values:
        for value, start_date in date_range_values.items():
            ms.select_date_range(value, start_date)
            ms.run()

    ms.close()
