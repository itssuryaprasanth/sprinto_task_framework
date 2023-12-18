import allure
from pages.flight_page import FlightSearchPage
from utilities.custom_logger import CustomLogger

log = CustomLogger()


class FlightSearchSteps:
    def __init__(self, driver):
        self.flight_search_step = FlightSearchPage(driver=driver)

    @allure.step("Open clear trip website")
    def open_clear_trip_website_in_browser(self):
        self.flight_search_step.open_clear_trip_in_browser()

    @allure.step("Searching for flights")
    def search_for_flights(self, where, data) -> None:
        self.flight_search_step.search_for_flights(where, data)

    @allure.step("Click on search flights button")
    def click_on_search_flights_button(self) -> None:
        self.flight_search_step.click_on_search_flights_button()

    @allure.step("Search day from calendar")
    def search_day_from_calendar(self, days) -> None:
        self.flight_search_step.search_day_from_calendar(no_days=days)

    @allure.step("Select cheapest flight")
    def select_cheapest_flight(self) -> None:
        self.flight_search_step.select_cheapest_flight()