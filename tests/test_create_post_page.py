"""Tests related to post create page"""
import allure
import pytest

from constants.base import BaseConstants
from constants.text_presets import UA_TEXT
from pages.create_post_page import UpsertPostPage
from pages.hello_user_page import HelloUserPage
from pages.post_page import PostPage
from pages.profile_page import ProfilePage
from pages.start_page import StartPage
from pages.utils import User, create_driver, random_num, random_str, random_text


@pytest.mark.parametrize("browser", BaseConstants.BROWSER_LIST_UNDER_TEST)
class TestCreatePostPage:
    """Tests related to post create page"""

    # pylint: disable=no-self-use,unused-argument
    @pytest.fixture(scope="function")
    def start_page(self, browser):
        """Start page object fixture"""
        driver = create_driver(browser)
        yield StartPage(driver)
        driver.close()

    @allure.feature("Create Post Page")
    @allure.story("Test create post as signed up user")
    def test_create_post(self, start_page, signed_in_user):
        """
        - Pre-requirements:
            - SignIn/Up as a user
        - Steps:
            - Create post
            - Verify message
        """
        # Create post
        post_create_page = signed_in_user.header.navigate_to_create_post()
        post_create_page.create_post(
            title=random_text(3), content=random_text(30, UA_TEXT)
        )

        # Verify message
        post_create_page.verify_message_text()

    def test_update_post(self, start_page: StartPage, user_with_post: User):
        """
        - Pre-conditions:
            - SignUp as a user
            - Create a post
        - Steps:
            - Sign in as the user
            - Navigate to profile page
            - Find post (click on it)
            - Click edit
            - Update title & body
            - Verify success message
            - Navigate to profile page
            - Find post (click on it)
            - Verify posts data
        """
        # Sign in as the user
        hello_user_page: HelloUserPage = start_page.sign_in(user_with_post)

        # Navigate to profile page
        profile_page: ProfilePage = hello_user_page.header.navigate_to_profile(
            user_with_post.username
        )

        # Find post (click on it)
        post_page: PostPage = profile_page.navigate_to_the_post(
            user_with_post.posts[0]
        )

        # Click edit
        upsert_post_page: UpsertPostPage = post_page.edit_post()

        # Update title & body
        title = f"{random_str()}-{random_num()}"
        content = random_text(30, UA_TEXT)
        upsert_post_page.update_post(title, content)
        upsert_post_page.verify_update_message_text()

        # Navigate to profile page
        profile_page: ProfilePage = upsert_post_page.header.navigate_to_profile(
            user_with_post.username
        )

        # Find post (click on it)
        post_page: PostPage = profile_page.navigate_to_the_post(title)

        # Verify posts data
        post_page.verify_post_data(title, content)

    def test_delete_post(self, start_page: StartPage, user_with_post: User):
        """
        - Pre-conditions:
            - Sign up as a user
            - Create post
        - Steps:
            - Sign in as the user
            - Navigate to profile page
            - Find post (click on it)
            - Delete post
            - Verify success delete message
            - Verify posts tab text (Posts: 0)
            - Verify post is not present on page
        """
        # Sign in as the user
        hello_user_page: HelloUserPage = start_page.sign_in(user_with_post)

        # Navigate to profile page
        profile_page: ProfilePage = hello_user_page.header.navigate_to_profile(
            user_with_post.username
        )

        # Find post (click on it)
        post_page: PostPage = profile_page.navigate_to_the_post(
            user_with_post.posts[0]
        )

        # # Delete post
        profile_page: ProfilePage = post_page.delete_post()

        # # Verify success delete message
        profile_page.verify_deleted_message_text()

        # Verify posts tab text (Posts: 0)
        profile_page.verify_posts_count(0)

        # Verify post is not present on page
        profile_page.verify_post_not_present(user_with_post.posts[0])
