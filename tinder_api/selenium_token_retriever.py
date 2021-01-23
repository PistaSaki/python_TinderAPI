from pathlib import Path

from seleniumwire import webdriver
from seleniumwire.webdriver import Chrome as WebDriver


def _start_driver(path_to_chromedriver) -> WebDriver:
    options = webdriver.ChromeOptions()
    options.add_argument(
        'user-agent = Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36')
    driver = webdriver.Chrome(chrome_options=options, executable_path=str(path_to_chromedriver))
    return driver


def _login_phone(driver: WebDriver) -> None:
    """Login to tinder using phone number and email."""
    driver.get('https://tinder.com')
    driver.implicitly_wait(20)
    login_button = driver.find_element_by_xpath(
        '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button')
    login_button.click()
    print("Now manually login with phone number.")


def _find_token(driver: WebDriver) -> str:
    driver.get('https://tinder.com/app/recs')
    for request in reversed(driver.requests):
        for key, value in request.headers.items():
            if key == 'X-Auth-Token':
                return value

    raise Exception("did not find token")


class SeleniumTokenRetriever:
    def __init__(self, path_to_chromedriver: Path):
        self.driver: WebDriver = _start_driver(path_to_chromedriver)

    def login_phone(self) -> None:
        _login_phone(self.driver)

    def find_token(self) -> str:
        return _find_token(self.driver)
