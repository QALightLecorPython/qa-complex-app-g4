"""Profile Page Constants"""


# pylint: disable=too-few-public-methods
class ProfilePageConstants:
    """Profile Page Constants"""

    FOLLOW_BUTTON_XPATH = ".//button[contains(text(),'Follow')]"
    FOLLOWERS_TAB_XPATH = ".//a[@href='/profile/{username}/followers']"
    FOLLOWERS_LIST_XPATH = ".//div[@class='list-group']//a"
    FOLLOWING_TAB_XPATH = ".//a[@href='/profile/{username}/following']"
    POSTS_TAB_XPATH = ".//a[@class='profile-nav-link nav-item nav-link active']"
    POSTS_LIST_XPATH = ".//div[@class='list-group']/a/strong"
    POST_DELETED_MESSAGE_XPATH = ".//div[@class='alert alert-success text-center']"
    POST_DELETED_MESSAGE_TEXT = "Post successfully deleted"
