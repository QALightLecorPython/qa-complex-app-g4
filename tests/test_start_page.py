"""Tests related to start page"""
import allure
import pytest
from allure_commons.types import Severity

from constants.base import BaseConstants
from pages.hello_user_page import HelloUserPage
from pages.start_page import StartPage
from pages.utils import User, create_driver


# @pytest.mark.parametrize("browser", BaseConstants.BROWSER_LIST_UNDER_TEST)
class TestStartPage:
    """Tests related to start page"""

    # pylint: disable=no-self-use
    @pytest.fixture(scope="function")
    def start_page(self):
        """Start page object fixture"""
        driver = create_driver(browser=BaseConstants.CHROME)
        yield StartPage(driver)
        driver.close()

    @allure.epic("Start Page")
    @allure.feature("Sign In")
    @allure.story("Test empty fields Sign In")
    @allure.severity(Severity.BLOCKER)
    def test_empty_fields_login(self, start_page: StartPage):
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

    @allure.epic("Start Page")
    @allure.feature("Sign In")
    @allure.story("Test invalid Sign In")
    @allure.severity(Severity.CRITICAL)
    def test_invalid_login(self, start_page: StartPage, random_user: User):
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

    @allure.epic("Start Page")
    @allure.feature("Sign Up")
    @allure.story("Test Sign Up")
    @allure.severity(Severity.CRITICAL)
    def test_register(self, start_page: StartPage, random_user: User):
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
        hello_user_page: HelloUserPage = start_page.sign_up_and_verify(
            random_user
        )

        # Verify registration is successful
        hello_user_page.verify_success_sign_up(username=random_user.username)

    @allure.epic("Start Page")
    @allure.feature("Sign Up")
    @allure.story("Test Sign In as signed up user")
    @allure.severity(Severity.NORMAL)
    def test_sign_in(self, signed_out_user: StartPage, random_user: User):
        """
        - Pre-conditions:
            - Sign up as a user
            - Logout
        - Steps:
            - Sign in as the user
            - Verify the result
        """
        # Sign in as the user
        hello_user_page: HelloUserPage = signed_out_user.sign_in(random_user)
        # Verify the result
        hello_user_page.verify_success_sign_up(username=random_user.username)

    @pytest.mark.parametrize(
        "user, text",
        [
            (
                    User(username="User123", email="user123@mail.com"),
                    "Password must be at least 12 characters.",
            ),
            (
                    User(username="User123", password="wncgficf453nc7"),
                    "You must provide a valid email address.",
            ),
            (
                    User(email="user123@mail.com", password="nc273rctw499m"),
                    "Username must be at least 3 characters.",
            ),
        ],
    )
    def test_sign_up_fields_validation(self, start_page, user, text):
        """
        - Pre-conditions:
            - Open start page
        - Steps:
            - Fill 2/3 fields
            - Click SignUp button
            - Verify error message text
        """
        # Try to sign up
        start_page.sign_up(user)
        # Verify error message text
        start_page.verify_sign_up_validation_error(text)
