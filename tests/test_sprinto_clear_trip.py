from fixtures.set_environment import create_environment
from steps.common_steps import FlightSearchSteps


def test_search_for_cheap_flights(create_environment):
    driver = create_environment.get_driver()
    search_steps = FlightSearchSteps(driver)
    try:
        search_steps.open_clear_trip_website_in_browser()
        search_steps.search_for_flights(where='From', data='Bangalore')
        search_steps.search_for_flights(where='To', data='New Delhi')
        search_steps.search_day_from_calendar(days=7)
        search_steps.click_on_search_flights_button()
        search_steps.select_cheapest_flight()
    finally:
        driver.quit()
