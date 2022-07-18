from datetime import datetime

from behave import runner, step
from fixtures.base_fixtures import add_value_to_context, get_locator_value
from pages.search_car_page import SearchCarPage


@step("the user is on Search car page")
def step_impl(context: runner.Context):
    context.driver.get(context.base_url)
    context.page = SearchCarPage(context.driver)


@step('the user clicks on the "{locator_name}"')
def step_impl(context: runner.Context, locator_name: str) -> None:
    locator = get_locator_value(context, locator_name)
    context.page.click(locator)


@step('the user fills the "{locator_name}" field with "{input_value}" value')
def step_impl(context: runner.Context, locator_name: str, input_value: str) -> None:
    locator = get_locator_value(context, locator_name)
    context.page.input(locator, input_value)


@step('the user fills the "{locator_name}" date field with "{input_value}" value')
def step_impl(context: runner.Context, locator_name: str, input_value: str) -> None:
    locator = get_locator_value(context, locator_name)
    if input_value == "current_date":
        input_value = datetime.today().strftime("%Y-%m-%d")
    # Date input needs 6 characters for the year input,
    # the two zeros are a workaround for inserting the correct format date
    add_value_to_context(context, locator_name, input_value)
    context.page.input(locator, f"00{input_value}")


@step('the user selects the "{dropdown_name}" with "{dropdown_value}" value')
def step_impl(context: runner.Context, dropdown_name: str, dropdown_value: str) -> None:
    locator = get_locator_value(context, dropdown_name)
    context.page.select_value_from_dropdown(locator, dropdown_value)


@step('the user is redirected to the "{page_type:PageType}"')
def step_impl(context: runner.Context, page_type):
    context.page = page_type(context.driver)
