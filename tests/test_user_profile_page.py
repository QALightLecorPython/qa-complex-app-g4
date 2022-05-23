import pytest

from constants.base import BaseConstants
from constants.text_presets import UA_TEXT
from pages.start_page import StartPage
from pages.utils import User, create_driver, random_text, random_str, random_num


@pytest.mark.parametrize("browser", BaseConstants.BROWSER_LIST_UNDER_TEST)
class TestStartPage:

    @pytest.fixture(scope="function")
    def start_page(self, browser):
        driver = create_driver(browser=browser)
        yield StartPage(driver)
        driver.close()

    @pytest.fixture(scope="function")
    def user_with_post(self, start_page):
        user = User()
        user.fill_properties()
        # Sign Up
        hello_user_page = start_page.sign_up(user)
        # Create post
        post_create_page = hello_user_page.header.navigate_to_create_post()
        title = f"{random_str()}-{random_num()}"
        post_create_page.create_post(title=title, content=random_text(30, UA_TEXT))
        user.posts.append(title)
        post_create_page.header.logout()
        return user

    def test_follow_user(self, user_with_post, signed_in_user, random_user):
        """
        - Pre-conditions:
            - Create user1
            - Add post for user1
            - Create user2
        - Steps:
            - Search for user1's post as user2
            - Move to post page
            - Move to user1 page
            - Follow user1 as user2
            - Verify user1 followers
            - Move to user2 profile
            - Verify user2 followings
        """
        hello_user_page = signed_in_user

        # Search for user1's post as user2
        # Move to post page
        post_page = hello_user_page.header.navigate_to_post_by_title(user_with_post.posts[0])

        # Move to user1 page
        profile_page = post_page.navigate_to_user_profile(user_with_post.username)

        # Follow user1 as user2
        # Verify user1 followers
        profile_page.follow_user_and_verify(user_with_post.username, random_user.username)

        # Move to user2 profile
        profile_page.header.navigate_to_profile(random_user.username)

        # Verify user2 followings
        profile_page.verify_followings(random_user.username, user_with_post.username)
