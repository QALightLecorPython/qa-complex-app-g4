"""Header Element Constants"""


# pylint: disable=too-few-public-methods
class HeaderConstants:
    """Header Element Constants"""

    CREATE_POST_BUTTON_XPATH = ".//a[@href='/create-post']"
    SIGN_OUT_BUTTON_XPATH = ".//button[text()='Sign Out']"
    SEARCH_ICON_XPATH = ".//a[@href='#']"
    SEARCH_TEXT_FIELD_XPATH = ".//input[@id='live-search-field']"
    SEARCH_RESULT_TITLE_XPATH = ".//strong[text()='{title}']"
    MY_PROFILE_BUTTON_XPATH = ".//a[@href='/profile/{username}']"
    CHAT_BUTTON_XPATH = ".//*[@data-icon='comment']"
