class ProfilePageConstants:
    FOLLOW_BUTTON_XPATH = ".//button[contains(text(),'Follow')]"
    FOLLOWERS_TAB_XPATH = ".//a[@href='/profile/{username}/followers']"
    FOLLOWERS_LIST_XPATH = ".//div[@class='list-group']//a"
    FOLLOWING_TAB_XPATH = ".//a[@href='/profile/{username}/following']"
