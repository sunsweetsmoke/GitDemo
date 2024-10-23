from email.policy import default

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default= "Chrome")

@pytest.fixture(scope="class")
def setup(request):

    global driver

    print("\n Im in fixture")
    browser_name = request.config.getoption("browser_name")

    if browser_name == "Chrome":
        chrome_opt = webdriver.ChromeOptions()
        chrome_opt.add_argument("--start-maximized")
        chrome_opt.add_argument("--ignore-certificate-errors")
        service_obj = Service(r'C:\chromedriver-win64\chromedriver-win64\chromedriver.exe')
        driver = webdriver.Chrome(service=service_obj, options=chrome_opt)
    elif browser_name == "Firefox":
        #firefox invocation
        pass

    chrome_opt = webdriver.ChromeOptions()
    chrome_opt.add_argument("--start-maximized")
    chrome_opt.add_argument("--ignore-certificate-errors")
    service_obj = Service(r'C:\chromedriver-win64\chromedriver-win64\chromedriver.exe')
    driver = webdriver.Chrome(service=service_obj, options=chrome_opt)
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    request.cls.driver = driver
    yield
    driver.close()

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
        driver.get_screenshot_as_file(name)