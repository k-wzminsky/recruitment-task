import typing
from datetime import datetime, timedelta

from behave import runner
from selenium.webdriver.remote import webelement


def add_value_to_context(
    context: runner.Context, variable_name: str, value: str
) -> None:
    split_value = variable_name.split(".")
    key = split_value[1].lower()
    setattr(context, key, value)


def get_locator_value(context: runner.Context, locator: str) -> str:
    split_locator = locator.split(".")
    obj = context.page
    for element in split_locator:
        obj = getattr(obj, element)
    return obj


def get_table_index_from_element_text(locator: webelement.WebElement) -> str:
    return locator.text.split()[0]


def calculate_future_date_from_current(days: int) -> str:
    current_date = datetime.today().strftime("%Y-%m-%d")
    date = datetime.strptime(current_date, "%Y-%m-%d")
    future_date = date + timedelta(days=days)
    final_date = datetime.strftime(future_date, "%Y-%m-%d")
    return final_date


def clear_price_value(value: str) -> int:
    clear_value = int(value.replace("$", ""))
    return int(clear_value)
