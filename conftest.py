import datetime
import os

import pytest

from constants.base import BaseConstants
from pages.hello_user_page import HelloUserPage
from pages.start_page import StartPage
from pages.utils import User


# pylint: disable=unused-argument
def pytest_sessionstart(session):
    os.environ["PATH"] = os.environ["PATH"] + f":{os.path.abspath(BaseConstants.DRIVERS_PATH)}"


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Preserve screenshot on fail"""
    outcome = yield
    result = outcome.get_result()

    if result.failed:
        driver = [item.funcargs[arg] for arg in item.funcargs if arg.endswith("_page")][0].driver
        file_name = f"{item.name}_{datetime.datetime.today().strftime('%Y-%m-%d_%H:%M:%S')}.png"
        file_path = "/Users/deniskondratuk/PycharmProjects/qa-complex-app-g4/screenshots"
        driver.save_screenshot(os.path.join(file_path, file_name))


@pytest.fixture(scope="function")
def random_user() -> User:
    user = User()
    user.fill_properties()
    return user


@pytest.fixture(scope="function")
def signed_in_user(start_page, random_user) -> HelloUserPage:
    hello_user_page = start_page.sign_up(random_user)
    return hello_user_page


@pytest.fixture(scope="function")
def signed_out_user(signed_in_user) -> StartPage:
    return signed_in_user.header.logout()
