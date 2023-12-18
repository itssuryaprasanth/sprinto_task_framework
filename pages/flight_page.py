from base.flight_search_base import FlightSearchBase
from helpers.json_helper import ObjFromJson


class FlightSearchPage(FlightSearchBase):
    def __init__(self, driver):
        self.json_obj = ObjFromJson()
        page_definition: dict = {
            "WhereFrom": self.json_obj.get_selected_locator(value="WhereFrom"),
            "WhereTo": self.json_obj.get_selected_locator(value="WhereTo"),
            "AirPortList": self.json_obj.get_selected_locator(value="AirPortList"),
            "SearchFlights": self.json_obj.get_selected_locator(value="SearchFlights"),
            "ClosePopup": self.json_obj.get_selected_locator(value="ClosePopup"),
            "DaySelect": self.json_obj.get_selected_locator(value="DaySelect"),
            "FlightsPrices": self.json_obj.get_selected_locator(value="FlightsPrices"),
            "StartDate": self.json_obj.get_selected_locator(value="StartDate")
        }
        super().__init__(driver, page_definition)
