import boto3
from selenium import webdriver
ARN = "arn:aws:devicefarm:us-west-2:233282665783:testgrid-project:9e4916f6-3052-4ef7-af6f-a696c0670c61"
def get_browser(browser):
    devicefarm_client = boto3.client("devicefarm", region_name="us-west-2")
    testgrid_url_response = devicefarm_client.create_test_grid_url(
    projectArn=ARN,
    expiresInSeconds=300)
    if browser == 'Chrome':
        driver = webdriver.Remote(testgrid_url_response["url"], webdriver.DesiredCapabilities.CHROME)
    elif browser == 'Firefox':
        driver = webdriver.Remote(testgrid_url_response["url"], webdriver.DesiredCapabilities.FIREFOX)
    elif browser == 'Ie':
        driver = webdriver.Remote(testgrid_url_response["url"], webdriver.DesiredCapabilities.INTERNETEXPLORER)
    elif browser == 'Edge':
        driver = webdriver.Remote(testgrid_url_response["url"], webdriver.DesiredCapabilities.EDGE)
    elif browser == 'Safari':
        driver = webdriver.Remote(testgrid_url_response["url"], webdriver.DesiredCapabilities.SAFARI)
    driver.implicitly_wait(30)
    driver.maximize_window()
    return driver