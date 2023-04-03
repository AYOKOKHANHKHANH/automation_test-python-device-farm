# Readme
Hello, I'm Pony. I built this source code to practice automation testing for web running on cloud environment. Basically, It's not defferent my old source. However, This source will be run on Device farm AWS. This makes the device cross-browser testable without having to install it. Below is the description and how to run the code. Please watch video in demo_video to better understand how to operate

## Require
 - Python 3 (new version)
 - Create environment on Windows using CMD(run as admin)
    + Install virtualenv
        $ python -m pip install --user virtualenv
    + Create a virtual environment
        $python -m venv venv
    + Activate a virtual environment
        $ .\venv\Scripts\activate
    + Leave the virtual environment
        $ deactivate

 - Install requirments.txt file
    $ pip install -r requirements.txt

 - Check your project's Amazon Resource Name (ARN) in ./manages/driverManages.py

 ## Run test
    - Browser list: Chrome, Edge, Firefox, Safari(Mac), Opera, Internet Explore. Default is Chrome
    - Run without pytest:
        $ pytest main.py --browser=<Browser Name>
    - Run with pytest
        $ pytest main.py

 ## Test Report
    - pytest-html, allure-pytest:
        $ pytest -v -s --alluredir=allure\allure-report --html=.\report\report.html main.py
    - Open allure
        $ allure serve <path allure-report folder>

## Discription
    - allure/allure report: Contain test result allure - It is created after run --alluredir=\allure-report
    - report/report.html: Contain test result is html file - It is created after run --html=.\report\report.html
    - data: Contain data as url, email,...
    (change)- manages/driverManages: Init browser, connect to AWS (ARN)
    - locators: Contain element locator: Id, Name, Css-selector, Class, Xpath,...
    - pages: Contain Object element
    - tests: Contain event, test case
    - conftest.py: config parameters for pytest (--browser)
    - main.py: Testsuite, executable file
    - requirments.txt: framework need to be install