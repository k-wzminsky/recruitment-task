import assertions
from behave import runner, step


@step("the model name is correctly displayed")
def step_impl(context: runner.Context):
    model_name = context.page.get(context.page.Misc.HEADER).text
    assertions.compare_values(model_name, context.table_model)


@step("the correct company name is displayed")
def step_impl(context: runner.Context):
    company_name = context.page.get(context.page.Misc.COMPANY_NAME).text
    expected_company = f"Company: {context.table_company_name}"
    assertions.compare_values(company_name, expected_company)


@step("the correct rent details are displayed")
def step_impl(context: runner.Context):
    rent_details_elements = context.page.get_all(context.page.Misc.RENT_DETAILS)
    rent_details = []
    for detail in rent_details_elements:
        rent_details.append(detail.text)
    expected_price_per_day = f"Price per day: {context.price_per_day}"
    expected_location = f"Location: {context.table_country}, {context.table_city}"
    expected_license_plate = f"License plate: {context.table_plate_number}"
    assertions.expected_in_displayed(expected_price_per_day, rent_details)
    assertions.expected_in_displayed(expected_location, rent_details)
    assertions.expected_in_displayed(expected_license_plate, rent_details)


@step("the pickup/dropoff dates are correctly displayed")
def step_impl(context: runner.Context):
    pickup_date_value = context.page.get(context.page.Misc.PICKUP_DATE_TEXT).text
    dropoff_date_value = context.page.get(context.page.Misc.DROP_OFF_DATE_TEXT).text
    assertions.expected_in_displayed(context.pick_up_date, pickup_date_value)
    assertions.expected_in_displayed(context.drop_off_date, dropoff_date_value)


@step(
    'the correct "{company_details}" company name, rent details and dates are displayed'
)
def step_impl(context: runner.Context, company_details: str):
    context.execute_steps(
        """
        Then the model name is correctly displayed
        And the correct company name is displayed
        And the correct rent details are displayed
        And the pickup/dropoff dates are correctly displayed
        """
    )
