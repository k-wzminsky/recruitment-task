import typing

import assertions
from behave import runner, step
from fixtures import base_fixtures
from fixtures.base_fixtures import get_table_index_from_element_text
from locator_formatters import FormattedLocator


@step('the users sees the displayed list of "{available_cars_amount:d}" available cars')
def step_impl(context: runner.Context, available_cars_amount):
    rows_locator = context.page.Misc.TABLE_ROWS
    displayed_elements = len(context.page.get_all(rows_locator))
    assertions.compare_values(displayed_elements, available_cars_amount)


@step(
    'the user fills the "{locator_name}" date field with "{days:d}" later than pick-off date'
)
def step_impl(context: runner.Context, locator_name: str, days: int) -> None:
    locator = base_fixtures.get_locator_value(context, locator_name)
    input_value = base_fixtures.calculate_future_date_from_current(days)
    context.page.input(locator, f"00{input_value}")


@step('the user gets the price per day for car with "{plate_number}" plate number')
def step_impl(context: runner.Context, plate_number: str) -> None:
    headers_positions = get_header_positions(context)
    row_locator = context.page.Misc.TABLE_CELL_BY_TD.formatted(td_text=plate_number)
    not_formatted_cell_locator = context.page.Misc.TABLE_CELL_BY_INDEX
    row_element = context.page.get(row_locator)
    table_index = get_table_index_from_element_text(row_element)
    price_per_day_locator = not_formatted_cell_locator.formatted(
        table_index=table_index, header_index=headers_positions["Price per day"]
    )
    context.price_per_day = context.page.get(price_per_day_locator).text


@step('the user clicks on the Rent button for car with "{plate_number}" plate number')
def step_impl(context: runner.Context, plate_number: str) -> None:
    button_locator = context.page.Buttons.TABLE_RENT_BUTTON_BY_TD.formatted(
        td_text=plate_number
    )
    context.page.click(button_locator)


@step(
    'the users sees the list of cars with correct calculated price for amount of "{days:d}" days'
)
def step_impl(context: runner.Context, days: int):
    headers_positions = get_header_positions(context)
    rows_locator = context.page.get_all(context.page.Misc.TABLE_ROWS)
    not_formatted_cell_locator = context.page.Misc.TABLE_CELL_BY_INDEX
    for row in rows_locator:
        # The first part of webelement of attribute 'text' is table index number (# header)
        table_index = get_table_index_from_element_text(row)
        price_per_day_locator = not_formatted_cell_locator.formatted(
            table_index=table_index, header_index=headers_positions["Price per day"]
        )
        price_locator = not_formatted_cell_locator.formatted(
            table_index=table_index, header_index=headers_positions["Price"]
        )

        displayed_price_per_day = context.page.get(price_per_day_locator).text
        price_per_day = base_fixtures.clear_price_value(displayed_price_per_day)
        displayed_price = context.page.get(price_locator).text
        expected_price = count_rent_price(price_per_day, days)
        assertions.compare_values(displayed_price, expected_price)


def get_row_details(
    locator: FormattedLocator,
    table_index: int,
    headers_positions: typing.Dict,
    header_name: str,
):
    return locator.formatted(
        table_index=table_index, header_index=headers_positions[header_name]
    )


def get_header_positions(context: runner.Context) -> typing.Dict:
    headers_elements = context.page.get_all(context.page.Misc.TABLE_HEADERS)
    headers_positions = {}
    for index, header in enumerate(headers_elements):
        header_name = header.text
        headers_positions[header_name] = index
    return headers_positions


def count_rent_price(price_per_day: int, days: int) -> str:
    price = str(price_per_day * days) + "$"
    return price


@step(
    'the user selects "{plate_number}", "{model}" car in "{country}, {city} from "{company_name}"'
)
def step_impl(
    context: runner.Context,
    plate_number: str,
    model: str,
    country: str,
    city: str,
    company_name: str,
):
    context.execute_steps(
        f"""
        When the user selects the "Dropdowns.COUNTRY" with "{country}" value
        And the user selects the "Dropdowns.CITY" with "{city}" value
        And the user fills the "Inputs.MODEL" field with "{model}" value
        And the user fills the "Inputs.PICK_UP_DATE" date field with "current_date" value
        And the user fills the "Inputs.DROP_OFF_DATE" date field with "current_date" value
        And the user clicks on the "Buttons.SEARCH"
        And the user gets the price per day for car with "{plate_number}" plate number
        And the user clicks on the Rent button for car with "{plate_number}" plate number
        Then the users is redirected to the "RentDetailsPage"
        """
    )
