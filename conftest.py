"""Conftest"""
import datetime
import os

import pytest

from constants.base import BaseConstants
from constants.text_presets import UA_TEXT
from pages.hello_user_page import HelloUserPage
from pages.start_page import StartPage
from pages.utils import Post, User, random_num, random_str, random_text


# pylint: disable=redefined-outer-name, missing-function-docstring, unused-argument, import-outside-toplevel
def pytest_sessionstart(session):
    os.environ["PATH"] = (
            os.environ["PATH"] + f":{os.path.abspath(BaseConstants.DRIVERS_PATH)}"
    )


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Preserve screenshot on fail"""
    outcome = yield
    result = outcome.get_result()

    if result.failed:
        driver = [
            item.funcargs[arg] for arg in item.funcargs if arg.endswith("_page")
        ][0].driver
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
    hello_user_page = start_page.sign_up_and_verify(random_user)
    return hello_user_page


@pytest.fixture(scope="function")
def create_few_posts(random_user, signed_in_user):
    hello_user_page = signed_in_user
    # Prepare posts
    post_1 = Post()
    post_1.fill_properties()

    post_2 = Post()
    post_2.fill_properties()
    from constants.create_post_page import CreatePostPageConstants

    post_2.share_option = CreatePostPageConstants.SHARE_OPTION_GROUP_MESSAGE

    # Create posts
    for post in [post_1, post_2]:
        post_create_page = hello_user_page.header.navigate_to_create_post()
        post_create_page.create_post_with_share_option(post)
        random_user.posts.append(post)


@pytest.fixture(scope="function")
def user_with_post(start_page):
    user = User()
    user.fill_properties()
    # Sign Up
    hello_user_page = start_page.sign_up_and_verify(user)
    # Create post
    post_create_page = hello_user_page.header.navigate_to_create_post()
    title = f"{random_str()}-{random_num()}"
    post_create_page.create_post(title=title, content=random_text(30, UA_TEXT))
    user.posts.append(title)
    post_create_page.header.logout()
    return user


@pytest.fixture(scope="function")
def signed_out_user(signed_in_user) -> StartPage:
    return signed_in_user.header.logout()
