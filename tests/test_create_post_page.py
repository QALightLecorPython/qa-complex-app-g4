class TestCreatePostPage:

    def test_create_post(self, signed_in_user, random_user):
        """
        - Pre-requirements:
            - SignIn/Up as a user
        - Steps:
            - Create post
            - Verify message
        """
        # Create post
        post_create_page = signed_in_user.header.navigate_to_create_post()
        post_create_page.create_post(title="Title", content="Some content here..")

        # Verify message
        post_create_page.verify_message_text()
