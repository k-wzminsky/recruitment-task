# -- REGISTER TYPE-CONVERTER: With behave
import behave
import pages


def register_types() -> None:
    behave.register_type(PageType=parse_page_type)


def parse_page_type(page_name: str) -> None:
    return getattr(pages, page_name)
