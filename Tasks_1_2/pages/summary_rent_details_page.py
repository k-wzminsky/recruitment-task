from selenium.webdriver.common import by

from pages import rent_details_page, base_page


class SummaryRentDetailsPage(base_page.BasePage):

    class Misc(rent_details_page.RentDetailsPage.Misc):
        ALERT = (by.By.CSS_SELECTOR, 'h5.alert')

    class Buttons:
        SEARCH = (by.By.CSS_SELECTOR, 'button[type=submit]')

    class Inputs:
        NAME = (by.By.ID, 'name')
        LAST_NAME = (by.By.ID, 'last_name')
        CARD_NUMBER = (by.By.ID, 'card_number')
        EMAIL = (by.By.ID, 'email')



