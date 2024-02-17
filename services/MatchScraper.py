import time
from datetime import datetime
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import configparser

from DBHandler import DBHandler
from models.Match import Match


class MatchScraper:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.options = Options()

        self.url = config.get('DEFAULT', 'site_url')
        self.options.headless = config.getboolean('DEFAULT', 'headless')
        self.db_handler = DBHandler()
        self.current_date = None

        self.options.binary_location = config.get('DEFAULT', 'firefox_binary_location')
        self.driver = webdriver.Firefox(executable_path=config.get('DEFAULT', 'firefox_driver_path'),
                                        options=self.options)

    def open(self):
        self.driver.get(self.url)

    def run(self):
        table = self.try_or_fail_to_load_element('iddaa_ajaxtable')
        rows = table.find_elements(By.TAG_NAME, "tr")

        skip_chars = ['', '-']

        match_que = []

        for row in rows:
            if row.get_attribute("class") == "tablemainheader":
                self.current_date = row.text.strip()
            elif row.get_attribute("filtervalue") == "futbol ":
                cells = row.find_elements(By.TAG_NAME, "td")[:15]
                tur = cells[3].text.strip() if len(cells) > 2 else None
                cells_array = []
                for x in cells:
                    if x.text.strip() != "":
                        cells_array.append(x.text.strip())
                    else:
                        cells_array.append(None)
                if any(cells_array[i] in skip_chars for i in [7, 8, 9, 10]):
                    print(f'Match skipped {cells_array[4], cells_array[6]}')
                    continue
                data = {
                    "date": self.current_date ,
                    "time": cells_array[0] ,
                    "league": cells_array[2] ,
                    "tour": cells_array[3] ,
                    "home_team": cells_array[4] ,
                    "second_half": cells_array[5] ,
                    "away_team": cells_array[6] ,
                    "first_half": cells_array[7] ,
                    "odds_1": cells_array[8] ,
                    "odds_x": cells_array[9] ,
                    "odds_2": cells_array[10] ,
                    "under": cells_array[11] ,
                    "over": cells_array[12] ,
                    "both_teams_score": cells_array[13] ,
                    "no_goal": cells_array[14]
                }
                match = Match(data)
                match_que.append(match)
        self.db_handler.add_matches(match_que)

    def get_date_range_values(self):
        date_range_element = self.try_or_fail_to_load_element('iddaa_daterange')
        date_options = date_range_element.find_elements(By.TAG_NAME, 'option')
        date_values = {}

        for option in date_options:
            value = option.get_attribute('value')
            dates = option.get_attribute('dates')
            start_date = datetime.strptime(dates.split(',')[0], '%Y-%m-%d').strftime('%d.%m.%Y')
            end_date = datetime.strptime(dates.split(',')[-2], '%Y-%m-%d').strftime('%d.%m.%Y')
            self.db_handler.insert_week(start_date, end_date)
            date_values[value] = start_date

        return date_values

    def select_date_range(self, value, expected_date):
        date_range_select = self.driver.find_element(By.ID, 'iddaa_daterange')
        date_range_dropdown = Select(date_range_select)
        date_range_dropdown.select_by_value(value)

        time.sleep(5)
        while True:
            try:
                row = self.driver.find_element(By.XPATH, "//*[@id='iddaa_ajaxtable']/table/tbody/tr[6]")
                current_date = row.text.strip()
                if expected_date == current_date:
                    return True
            except NoSuchElementException:
                print("6. row couldn't be found. Retrying..")
                return False

    def select_all_dates(self):
        date_range_select = self.driver.find_element(By.ID, 'iddaa_dateselector')
        date_range_dropdown = Select(date_range_select)
        date_range_dropdown.select_by_value(str('*'))
        time.sleep(3)

    def try_or_fail_to_load_element(self, element_name):
        try:
            wait = WebDriverWait(self.driver, 10)
            print("Element is loading.. ")
            return wait.until(EC.presence_of_element_located((By.ID, element_name)))

        except TimeoutException:
            print("Element couldn't be loaded. Exiting..")

    def close(self):
        self.driver.quit()
