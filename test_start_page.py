import logging

import pytest
from selenium.webdriver.chrome.webdriver import WebDriver

from constants.base import BaseConstants
from pages.start_page import StartPage
from pages.utils import User


class TestStartPage:
    log = logging.getLogger("[StartPage]")

    @pytest.fixture(scope="function")
    def start_page(self):
        driver = WebDriver(executable_path=BaseConstants.DRIVER_PATH)
        driver.implicitly_wait(3)
        driver.get(BaseConstants.BASE_URL)
        yield StartPage(driver)
        driver.close()

    @pytest.fixture(scope="function")
    def random_user(self):
        user = User()
        user.fill_properties()
        return user

    @pytest.fixture(scope="function")
    def registered_user(self, start_page, random_user):
        start_page.sign_up(random_user)
        start_page.logout()
        return random_user

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
        start_page.sign_up(random_user)

        # Verify registration is successful
        start_page.verify_success_sign_up(username=random_user.username)

    def test_sign_in(self, start_page, registered_user):
        """
        - Pre-conditions:
            - Sign up as a user
            - Logout
        - Steps:
            - Sign in as the user
            - Verify the result
        """
        # Sign in as the user
        start_page.sign_in(registered_user)
        # Verify the result
        start_page.verify_success_sign_up(username=registered_user.username)
