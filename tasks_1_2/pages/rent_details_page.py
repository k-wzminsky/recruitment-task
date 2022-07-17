from pages import base_page
from selenium.webdriver.common import by


class RentDetailsPage(base_page.BasePage):
    class Misc:
        HEADER = (by.By.CSS_SELECTOR, "div.card-header")
        COMPANY_NAME = (by.By.CSS_SELECTOR, "div[id=content] h5.card-title")
        RENT_DETAILS = (by.By.CSS_SELECTOR, "div[id=content]  p")
        PICKUP_DATE_TEXT = (
            by.By.XPATH,
            '//div[@id="content"]//h6[contains(text(), "Pickup")]',
        )
        DROP_OFF_DATE_TEXT = (
            by.By.XPATH,
            '//div[@id="content"]//h6[contains(text(), "Dropoff")]',
        )

    class Buttons:
        RENT = (by.By.CSS_SELECTOR, "div a.btn")
