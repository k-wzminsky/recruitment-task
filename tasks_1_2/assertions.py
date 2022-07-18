import typing


def compare_values(
    displayed_value: typing.Union[str, int], expected_value: typing.Union[str, int]
) -> None:
    assert (
        displayed_value == expected_value
    ), f'The values are not that same. Is displayed: "{displayed_value}" but expected: "{expected_value}"'


def expected_in_displayed(
    expected_value: typing.Union[str, int],
    displayed_value: typing.Union[str, int, list],
) -> None:
    assert (
        expected_value in displayed_value
    ), f'The values are not matched. Displayed value: "{displayed_value}" does not contains: "{expected_value}"'
