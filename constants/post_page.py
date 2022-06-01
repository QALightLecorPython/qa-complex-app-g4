"""Post Page Constants"""


# pylint: disable=too-few-public-methods
class PostPageConstants:
    """Post Page Constants"""

    LINK_TO_USER_PROFILE_XPATH = ".//a[@href='/profile/{username}']"
    EDIT_POST_BUTTON_XPATH = ".//*[@data-icon='edit']"
    TITLE_TEXT_XPATH = ".//h2"
    CONTENT_TEXT_XPATH = ".//div[@class='container py-md-5 container--narrow']/div[3]/p"
    DELETE_POST_BUTTON_XPATH = ".//*[@data-icon='trash']"
