import pytest

from pages.utils import User


@pytest.fixture(scope="function")
def random_user():
    user = User()
    user.fill_properties()
    return user


@pytest.fixture(scope="function")
def signed_in_user(start_page, random_user):
    hello_user_page = start_page.sign_up(random_user)
    return hello_user_page


@pytest.fixture(scope="function")
def signed_out_user(signed_in_user):
    return signed_in_user.header.logout()
