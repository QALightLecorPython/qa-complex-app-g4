import pytest

from constants.base import BaseConstants
from pages.start_page import StartPage
from pages.utils import User, create_driver


@pytest.mark.parametrize("browser", BaseConstants.BROWSER_LIST_UNDER_TEST)
class TestStartPage:

    @pytest.fixture(scope="function")
    def start_page(self, browser):
        driver = create_driver(browser=browser)
        yield StartPage(driver)
        driver.close()

    def test_empty_fields_login(self, start_page):
        """
        - Pre-conditions:
            - Create driver
            - Open start page
        - Steps:
            - Clear field login
            - Clear field password
            - Click on 'Sign In' button
            - Verify error message
        """
        # Clear field login
        # Clear field password
        # Click on 'Sign In' button
        start_page.sign_in(User())

        # Verify error message
        start_page.verify_sign_in_error()

    def test_invalid_login(self, start_page, random_user):
        """
        - Pre-conditions:
            - Create driver
            - Open start page
        - Steps:
            - Fill field login
            - Fill field password
            - Click on 'Sign In' button
            - Verify error message
        """
        # Fill field login
        # Fill field password
        # Click on 'Sign In' button
        start_page.sign_in(random_user)

        # Verify error message
        start_page.verify_sign_in_error()

    def test_register(self, start_page, random_user):
        """
        - Pre-requirements:
            - Open start page
        - Steps:
            - Fill email, login and password fields
            - Click on Sign Up button
            - Verify registration is successful
        """
        # Fill email, login and password fields
        # Click on Sign Up button
        hello_user_page = start_page.sign_up(random_user)

        # Verify registration is successful
        hello_user_page.verify_success_sign_up(username=random_user.username)

    def test_sign_in(self, signed_out_user, random_user):
        """
        - Pre-conditions:
            - Sign up as a user
            - Logout
        - Steps:
            - Sign in as the user
            - Verify the result
        """
        # Sign in as the user
        hello_user_page = signed_out_user.sign_in(random_user)
        # Verify the result
        hello_user_page.verify_success_sign_up(username=random_user.username)
