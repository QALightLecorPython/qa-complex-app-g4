import logging
from time import sleep

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
        driver.get(BaseConstants.BASE_URL)
        yield StartPage(driver)
        driver.close()

    @pytest.fixture(scope="function")
    def random_user(self):
        return User()

    @pytest.fixture(scope="function")
    def registered_user(self, start_page, random_user):
        start_page.sign_up(random_user)
        sleep(1)
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
        start_page.sign_in()
        self.log.info("Empty string user tried to signed in")

        # Verify error message
        start_page.verify_sign_in_error()
        self.log.info("Error was verified")

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
        start_page.sign_in(username=random_user.username, password=random_user.password)
        self.log.info("Empty string user tried to signed in")

        # Verify error message
        start_page.verify_sign_in_error()
        self.log.info("Error was verified")

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
        self.log.info("User was registered")
        sleep(1)

        # Verify registration is successful
        start_page.verify_success_sign_up(username=random_user.username)
        self.log.info("Registration for user '%s' was success and verified", random_user.username)

    def test_sign_in(self, start_page, registered_user):
        """
        - Pre-conditions:
            - Sign up as a user
            - Logout
        - Steps:
            - Sign in as the user
            - Verify the result
        """
        start_page.sign_in(username=registered_user.username, password=registered_user.password)
        self.log.info("User '%s' signed in", registered_user.username)

        start_page.verify_success_sign_up(username=registered_user.username)
        self.log.info("Message was verified")
