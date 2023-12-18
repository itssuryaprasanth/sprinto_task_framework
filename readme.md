# Automation Demo with Pytest

### Getting Started

To begin, please install all required python packages through requirements.txt.
    # install command ==> pip install -r requirements.txt

Please keep the latest chrome driver version in %PYTHONPATH%/Scripts/chromedriver.exe
Download the latest version from this link ==> https://chromedriver.chromium.org/downloads

Download the allure reporting tool from ==> https://github.com/allure-framework/allure2/releases and set environment path

This framework is designed by keeping scalable & robustness as a first priority. Each component having its own uniqueness.

#### features/base/flight_search_base.py => Contains actual implementation.
#### features/steps/common_steps.py => Contains steps of implementation and driver class object initializer.
#### fixtures/set_environment.py => It will create chrome driver instance and supplied to common_steps.py class constructor
#### helpers/json_helper.py => Loads the json file and transfer the instance where ever it's created
#### objectsrepository/trip_objects.json => Contains object of the web page in form of xpath etc...
#### pages/flight_page.py => Contains dictionary of web pages elements

flight_search_base instance is not exposed to common_steps class, 
instance created in common_steps class is flight_page class, flight_page class is inherits flight_search_base class.
Here actual implementation of base methods are not exposed to common_steps.(**inspired by Abstraction**) 

#### tests ==> contains test file

#### utilities/custom_logger.py =>> Logger class to record each and every action

**custom_logger.py is implemented in Singleton design pattern**

#### wrappers/browser_driver.py ==> Contains driver methods implementation

#### .env file contains all the global variables values



**`How to run the tests?`**

Change the directory to features/tests

`pytest <test_name> --alluredir=C:\Windows\Temp\Sprinto\allure-reports`

