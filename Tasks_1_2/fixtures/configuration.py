import behave
from behave import runner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def driver(context: runner.Context):
    width = 1920
    height = 1080
    chrome_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    chrome_driver.set_window_size(width, height)
    return chrome_driver


@behave.fixture
def base_url(context: runner.Context) -> str:
    return get_user_argument(context, "base_url", required=True)


def get_user_argument(context: runner.Context, argument: str, required: bool = False) -> str:
    argument_value = context.config.userdata.get(argument)
    if not required or required and argument_value is not None:
        return argument_value
    raise AttributeError(f'Argument {argument} is mandatory')
