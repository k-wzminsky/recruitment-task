import typing
from selenium.common import TimeoutException
from selenium.webdriver.remote import webelement
from selenium.webdriver.support import expected_conditions, ui, wait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    WAIT_TIME = 5  # default set time (in seconds) to wait for element

    def click(self, locator: tuple, wait_seconds: int = WAIT_TIME) -> None:
        element = wait.WebDriverWait(driver=self.driver, timeout=wait_seconds).until(
            expected_conditions.element_to_be_clickable(locator)
        )
        element.click()

    def get(
        self, locator: tuple, wait_seconds: int = WAIT_TIME
    ) -> webelement.WebElement:
        element = wait.WebDriverWait(driver=self.driver, timeout=wait_seconds).until(
            expected_conditions.visibility_of_element_located(locator)
        )
        return element

    def get_all(
        self, locator: tuple, wait_seconds: int = WAIT_TIME
    ) -> typing.List[webelement.WebElement]:
        element = wait.WebDriverWait(driver=self.driver, timeout=wait_seconds).until(
            expected_conditions.visibility_of_all_elements_located(locator)
        )
        return element

    def input(self, locator: tuple, value: str) -> None:
        element = self.get(locator)
        element.send_keys(value)

    def select_value_from_dropdown(self, locator: tuple, value: str) -> None:
        element = self.get(locator)
        ui.Select(element).select_by_visible_text(value)

    def is_displayed(self, locator: tuple) -> bool:
        try:
            self.get(locator, wait_seconds=1)
            return True
        except TimeoutException:
            return True
