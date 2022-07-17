from behave import runner, step


@step('the correct "{company_details}" company summary details are displayed')
def step_impl(context: runner.Context, company_details: str):
    context.execute_steps(
        """
        Then the correct company name is displayed
        And the correct rent details are displayed
        And the pickup/dropoff dates are correctly displayed
        """
    )


@step("there are no inputs error messages displayed")
def step_impl(context: runner.Context):
    is_alert_displayed = context.page.is_displayed(context.page.Misc.ALERT)
    assert is_alert_displayed, "The input alert is displayed"
