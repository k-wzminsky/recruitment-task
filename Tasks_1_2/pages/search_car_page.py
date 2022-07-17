from selenium.webdriver.common import by

from locator_formatters import FormattedLocator
from pages import base_page


class SearchCarPage(base_page.BasePage):

    class Misc:
        TABLE_ROWS = (by.By.CSS_SELECTOR, 'table[id=search-results] tbody tr')
        TABLE_HEADERS = (by.By.CSS_SELECTOR, 'table[id=search-results] thead tr th')
        TABLE_CELL_BY_INDEX = FormattedLocator(by.By.XPATH, '//tbody/tr/th[text()="{table_index}"]/following-sibling::td[{header_index}]')
        TABLE_CELL_BY_TD = FormattedLocator(by.By.XPATH, '//table/tbody/tr[td[text()="{td_text}"]]')

    class Buttons:
        SEARCH = (by.By.CSS_SELECTOR, 'button[type=submit]')
        TABLE_RENT_BUTTON_BY_TD = FormattedLocator(by.By.XPATH, '//table/tbody/tr[td[text()="{td_text}"]]//a')

    class Dropdowns:
        COUNTRY = (by.By.ID, 'country')
        CITY = (by.By.ID, 'city')

    class Inputs:
        DROP_OFF_DATE = (by.By.ID, 'dropoff')
        PICK_UP_DATE = (by.By.ID, 'pickup')
        MODEL = (by.By.ID, 'model')
