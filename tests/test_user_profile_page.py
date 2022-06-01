"""Tests related o profile page"""
import random

import allure
import pytest

from constants.base import BaseConstants
from pages.hello_user_page import HelloUserPage
from pages.post_page import PostPage
from pages.profile_page import ProfilePage
from pages.start_page import StartPage
from pages.utils import User, create_driver, random_text


@pytest.mark.parametrize("browser", BaseConstants.BROWSER_LIST_UNDER_TEST)
class TestUserProfilePage:
    """Tests related o profile page"""

    # pylint: disable=no-self-use,unused-argument
    @pytest.fixture(scope="function")
    def start_page(self, browser):
        """Start page object fixture"""
        driver = create_driver(browser=browser)
        yield StartPage(driver)
        driver.close()

    @allure.feature("User Profile Page")
    @allure.story("Test follow user")
    def test_follow_user(
            self,
            start_page: StartPage,
            user_with_post: User,
            signed_in_user: HelloUserPage,
            random_user: User,
    ):
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
        hello_user_page: HelloUserPage = signed_in_user

        # Search for user1's post as user2
        # Move to post page
        with allure.step(f"Navigate to post by title '{user_with_post.posts[0]}'"):
            post_page: PostPage = hello_user_page.header.navigate_to_post_by_title(user_with_post.posts[0])

        # Move to user1 page
        with allure.step(f"Navigate to user profile ({user_with_post.username})"):
            profile_page: ProfilePage = post_page.navigate_to_user_profile(user_with_post.username)

        # Follow user1 as user2
        # Verify user1 followers
        with allure.step("Follow user and verify"):
            profile_page.follow_user_and_verify(user_with_post.username, random_user.username)

        # Move to user2 profile
        with allure.step(f"Navigate to user profile ({random_user.username})"):
            profile_page.header.navigate_to_profile(random_user.username)

        # Verify user2 followings
        with allure.step("Verify following tab"):
            profile_page.verify_followings(random_user.username, user_with_post.username)

    def test_chat(self, start_page: StartPage, signed_in_user: HelloUserPage):
        """
        - Pre-conditions:
            - Sign up as new user
        - Steps:
            - Open chat
            - Put some text in the chat
            - Verify that message appears
            - Put one more message
            - Verify that all messages present in chat
        """
        hello_user_page: HelloUserPage = signed_in_user

        # Open chat
        hello_user_page.header.open_chat()

        # Put some text in the chat
        expected_messages = [random_text(3)]
        hello_user_page.chat.send_message(expected_messages[0])

        # Verify that message appears
        hello_user_page.chat.verify_messages(expected_messages)

        # Put one more message
        for _ in range(25):
            expected_messages.append(random_text(random.randint(2, 7)))
            hello_user_page.chat.send_message(expected_messages[-1])

        # Verify that all messages present in chat
        hello_user_page.chat.verify_messages(expected_messages)

    def test_view_user_posts(self, random_user, create_few_posts, signed_in_user):
        """
        - Pre-conditions:
            - Sign up as a user
            - Create few posts (with different share options)
        - Steps:
            - Navigate to profile page
            - Verify posts count
            - Verify posts content
        """
        hello_user_page: HelloUserPage = signed_in_user

        # Navigate to profile page
        profile_page: ProfilePage = hello_user_page.header.navigate_to_profile(random_user.username)

        # Verify posts count
        assert profile_page.wait_until_displayed(xpath=profile_page.constants.POSTS_TAB_XPATH.format(username=random_user.username.lower())).text == "Posts: 2"
