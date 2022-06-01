"""Create Post Constants"""


# pylint: disable=too-few-public-methods
class CreatePostPageConstants:
    """Create Post Constants"""

    TITLE_FIELD_XPATH = ".//input[@id='post-title']"
    CONTENT_FIELD_XPATH = ".//textarea[@id='post-body']"
    SHARE_OPTION_DROP_DOWN_XPATH = ".//select[@id='select1']"
    SHARE_OPTION_MESSAGE_XPATH = ".//option[@value='{option}']"
    SHARE_OPTION_GROUP_MESSAGE = "Group Message"
    SHARE_OPTION_ALL_USERS = "All Users"
    SHARE_OPTION_ONE_PERSON = "One Person"
    SAVE_POST_BUTTON_XPATH = ".//button[text()='Save New Post']"
    UPDATE_POST_BUTTON_XPATH = ".//button[text()='Save Updates']"
    SUCCESS_MESSAGE_XPATH = ".//div[@class='alert alert-success text-center']"
    SUCCESS_MESSAGE_TEXT = "New post successfully created."
    SUCCESS_UPDATE_MESSAGE_TEXT = "Post successfully updated."
