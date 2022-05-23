import pytest

from constants.base import BaseConstants
from constants.text_presets import UA_TEXT
from pages.start_page import StartPage
from pages.utils import create_driver, random_text


@pytest.mark.parametrize("browser", BaseConstants.BROWSER_LIST_UNDER_TEST)
class TestCreatePostPage:
    @pytest.fixture(scope="function")
    def start_page(self, browser):
        driver = create_driver(browser)
        yield StartPage(driver)
        driver.close()

    def test_create_post(self, signed_in_user):
        """
        - Pre-requirements:
            - SignIn/Up as a user
        - Steps:
            - Create post
            - Verify message
        """
        # Create post
        post_create_page = signed_in_user.header.navigate_to_create_post()
        post_create_page.create_post(title=random_text(3), content=random_text(30, UA_TEXT))

        # Verify message
        post_create_page.verify_message_text()
