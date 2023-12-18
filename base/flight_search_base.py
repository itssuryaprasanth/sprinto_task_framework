import datetime
import os
from selenium.webdriver.common.action_chains import ActionChains
from utilities.custom_logger import CustomLogger
from time import sleep

log = CustomLogger()


# global variables


class FlightSearchBase:
    def __init__(self, driver, page_definition):
        self.driver = driver
        self.action = ActionChains(self.driver)
        self.where_from: dict = page_definition['WhereFrom']
        self.where_to: dict = page_definition['WhereTo']
        self.airport_list: dict = page_definition['AirPortList']
        self.search_flights: dict = page_definition['SearchFlights']
        self.days_select: dict = page_definition['DaySelect']
        self.flights_price: dict = page_definition['FlightsPrices']
        self.close_popup: dict = page_definition['ClosePopup']
        self.start_date: dict = page_definition['StartDate']

    def open_clear_trip_in_browser(self) -> None:
        log.debug("Open clear trip url in browser")
        self.driver.launch_url_in_browser(url=f"{os.getenv('BrowserURL')}")
        self.driver.maximize_browser()
        self.driver.click_element(self.close_popup)

    def search_for_flights(self, where, data) -> None:
        log.debug("Searching for flights with {0} {1}".format(where, data))
        flights_search_type = {'From': self.where_from, 'To': self.where_to}
        self.driver.input_text(element=flights_search_type.get(where), data=data)
        flight_list = self.driver.wait_and_get_element_list(element=self.airport_list)
        for listed_flight_names in flight_list:
            if str(listed_flight_names.text).__contains__(data):
                listed_flight_names.click()
                break

    def click_on_search_flights_button(self) -> None:
        log.debug("Click on search flights button")
        self.driver.click_element(self.search_flights)

    @staticmethod
    def get_date_after_one_week(days):
        today = datetime.datetime.now()
        one_week_delta = datetime.timedelta(days=days)
        one_week_later = today + one_week_delta
        formatted_date = one_week_later.strftime("%a %b %d %Y")
        return formatted_date, one_week_later

    @staticmethod
    def week_number_in_month(date):
        first_day = date.replace(day=1)
        day_of_month = date.day
        day_of_week = first_day.weekday()
        adjusted_day = day_of_month + day_of_week
        return (adjusted_day - 1) // 7 + 1

    def search_day_from_calendar(self, no_days) -> None:
        log.debug("Search day from calendar")
        self.driver.click_element(self.start_date)
        one_week_later_formatted, one_week_later_datetime = FlightSearchBase.get_date_after_one_week(no_days)
        week_in_month = FlightSearchBase.week_number_in_month(one_week_later_datetime)
        log.info("Date formatted ==> {}".format(one_week_later_formatted))
        self.days_select['value'] = str(self.days_select['value']).replace('{1}', str(one_week_later_formatted))
        self.days_select['value'] = str(self.days_select['value']).replace('{0}', str(week_in_month))
        self.driver.click_element(self.days_select)

    def select_cheapest_flight(self) -> None:
        log.debug("Select the cheapest flight rate")
        flights_results = min(set(self.driver.wait_and_get_element_list(self.flights_price)))
        log.info("Cheapest Flight rate is ==> " + flights_results)
