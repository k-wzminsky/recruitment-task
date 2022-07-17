from typing import NamedTuple

from selenium.webdriver.common import by


class FormattedLocator(NamedTuple):
    strategy: by.By
    locator: str

    def formatted(self, **kwargs):
        try:
            return FormattedLocator(
                strategy=self.strategy, locator=self.locator.format(**kwargs)
            )
        except KeyError as key_error:
            raise KeyError(f"Missing {key_error} in locator")
