class CreatePostPageConstants:
    TITLE_FIELD_XPATH = ".//input[@id='post-title']"
    CONTENT_FIELD_XPATH = ".//textarea[@id='post-body']"
    SAVE_POST_BUTTON_XPATH = ".//button[text()='Save New Post']"
    SUCCESS_MESSAGE_XPATH = ".//div[@class='alert alert-success text-center']"
    SUCCESS_MESSAGE_TEXT = "New post successfully created."
