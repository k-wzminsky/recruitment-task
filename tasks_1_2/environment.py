import behave
from behave import runner
from fixtures import configuration
from parsers import register_types

register_types()


def before_all(context: runner.Context):
    context.base_url = behave.use_fixture(configuration.base_url, context)
    context.driver = behave.use_fixture(configuration.driver, context)


def before_scenario(context: runner.Context, scenario):
    _add_table_to_context(context)


def after_all(context: runner.Context):
    context.driver.quit()


def _add_table_to_context(context: runner.Context) -> None:
    if context.active_outline:
        for index, heading in enumerate(context.active_outline):
            setattr(context, f"table_{context.active_outline.headings[index]}", heading)
