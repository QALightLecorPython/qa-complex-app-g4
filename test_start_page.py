import logging
import random
import string
from time import sleep

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class TestStartPage:
    log = logging.getLogger("[StartPage]")

    @staticmethod
    def random_num():
        """Generate random number"""
        return str(random.randint(111111, 999999))

    @staticmethod
    def random_str(length=5):
        """Generate random string"""
        return ''.join(random.choice(string.ascii_letters) for _ in range(length))

    def test_empty_fields_login(self):
        """
        - Create driver
        - Open start page
        - Clear field login
        - Clear field password
        - Click on 'Sign In' button
        - Verify error message
        """
        # Create driver
        driver = WebDriver(executable_path="/Users/deniskondratuk/PycharmProjects/qa-complex-app-g4/chromedriver")

        # Open start page
        self.log.info("Opening start page")
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")

        # Clear field login
        self.log.info("Cleaning login field")
        # - Find element
        login_field = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Username']")
        # - Clear
        login_field.clear()

        # Clear field password
        self.log.info("Cleaning password field")
        # - Find element
        password_field = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Password']")
        # - Clear
        password_field.clear()

        # Click on 'Sign In' button
        self.log.info("Going to click 'Sign In' button")
        driver.find_element(by=By.XPATH, value=".//button[text()='Sign In']").click()

        # Verify error message
        self.log.info("Verifying error message")
        error_message = driver.find_element(by=By.XPATH, value=".//div[@class='alert alert-danger text-center']")
        assert error_message.text == "Invalid username / pasword", "Text is not valid"

        # Close driver
        driver.close()

    def test_invalid_login(self):
        """
        - Create driver
        - Open start page
        - Fill field login
        - Fill field password
        - Click on 'Sign In' button
        - Verify error message
        """
        # Create driver
        driver = WebDriver(executable_path="/Users/deniskondratuk/PycharmProjects/qa-complex-app-g4/chromedriver")

        # Open start page
        self.log.info("Opening start page")
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")

        # Clear field login
        self.log.info("Filling login field")
        # - Find element
        login_field = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Username']")
        # - Clear
        login_field.clear()
        # - Fill
        login_field.send_keys("RandomName13")
        sleep(1)

        # Clear field password
        self.log.info("Filling password field")
        # - Find element
        password_field = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Password']")
        # - Clear
        password_field.clear()
        # - Fill
        password_field.send_keys("RandomPwd11")
        sleep(1)

        # Click on 'Sign In' button
        self.log.info("Going to click 'Sign In' button")
        driver.find_element(by=By.XPATH, value=".//button[text()='Sign In']").click()
        sleep(1)

        # Verify error message
        self.log.info("Verifying error message")
        error_message = driver.find_element(by=By.XPATH, value=".//div[@class='alert alert-danger text-center']")
        assert error_message.text == "Invalid username / pasword", "Text is not valid"

        # Close driver
        driver.close()

    def test_register(self):
        """
        - Open start page
        - Fill email, login and password fields
        - Click on Sign Up button
        - Verify registration is successful
        """
        # Create driver
        driver = WebDriver(executable_path="/Users/deniskondratuk/PycharmProjects/qa-complex-app-g4/chromedriver")

        # Open start page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com")
        self.log.debug("Open page")

        # Fill username
        user = self.random_str()
        username_value = f"{user}{self.random_num()}"
        username = driver.find_element(by=By.XPATH, value=".//input[@id='username-register']")
        username.clear()
        username.send_keys(username_value)

        # Fill email
        email_value = f"{user}{self.random_num()}@mail.com"
        email = driver.find_element(by=By.XPATH, value=".//input[@id='email-register']")
        email.clear()
        email.send_keys(email_value)

        # Fill password
        password_value = f"PwD{self.random_num()}"
        password = driver.find_element(by=By.XPATH, value=".//input[@id='password-register']")
        password.clear()
        password.send_keys(password_value)
        self.log.info("Fields were filled")
        sleep(1)

        # Click on Sign Up button
        driver.find_element(by=By.XPATH, value=".//button[@type='submit']").click()
        self.log.info("User was registered")
        sleep(1)

        # Verify register success
        hello_message = driver.find_element(by=By.XPATH, value=".//h2")
        assert username_value.lower() in hello_message.text
        assert hello_message.text == f"Hello {username_value.lower()}, your feed is empty."
        assert driver.find_element(by=By.XPATH, value=".//strong").text == username_value.lower()
        self.log.info("Registration for user '%s' was success and verified", username_value)

    def test_invalid_login_1(self):
        """
        - Create driver
        - Open start page
        - Fill field login
        - Fill field password
        - Click on 'Sign In' button
        - Verify error message
        """
        # Create driver
        driver = WebDriver(executable_path="/Users/deniskondratuk/PycharmProjects/qa-complex-app-g4/chromedriver")

        # Open start page
        self.log.info("Opening start page")
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")

        # Clear field login
        self.log.info("Filling login field")
        # - Find element
        login_field = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Username']")
        # - Clear
        login_field.clear()
        # - Fill
        login_field.send_keys("RandomName13")
        sleep(1)

        # Clear field password
        self.log.info("Filling password field")
        # - Find element
        password_field = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Password']")
        # - Clear
        password_field.clear()
        # - Fill
        password_field.send_keys("RandomPwd11")
        sleep(1)

        # Click on 'Sign In' button
        self.log.info("Going to click 'Sign In' button")
        driver.find_element(by=By.XPATH, value=".//button[text()='Sign In']").click()
        sleep(1)

        # Verify error message
        self.log.info("Verifying error message")
        error_message = driver.find_element(by=By.XPATH, value=".//div[@class='alert alert-danger text-center']")
        assert error_message.text == "Invalid username / pasword", "Text is not valid"

        # Close driver
        driver.close()

    def test_register_1(self):
        """
        - Open start page
        - Fill email, login and password fields
        - Click on Sign Up button
        - Verify registration is successful
        """
        # Create driver
        driver = WebDriver(executable_path="/Users/deniskondratuk/PycharmProjects/qa-complex-app-g4/chromedriver")

        # Open start page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com")
        self.log.debug("Open page")

        # Fill username
        user = self.random_str()
        username_value = f"{user}{self.random_num()}"
        username = driver.find_element(by=By.XPATH, value=".//input[@id='username-register']")
        username.clear()
        username.send_keys(username_value)

        # Fill email
        email_value = f"{user}{self.random_num()}@mail.com"
        email = driver.find_element(by=By.XPATH, value=".//input[@id='email-register']")
        email.clear()
        email.send_keys(email_value)

        # Fill password
        password_value = f"PwD{self.random_num()}"
        password = driver.find_element(by=By.XPATH, value=".//input[@id='password-register']")
        password.clear()
        password.send_keys(password_value)
        self.log.info("Fields were filled")
        sleep(1)

        # Click on Sign Up button
        driver.find_element(by=By.XPATH, value=".//button[@type='submit']").click()
        self.log.info("User was registered")
        sleep(1)

        # Verify register success
        hello_message = driver.find_element(by=By.XPATH, value=".//h2")
        assert username_value.lower() in hello_message.text
        assert hello_message.text == f"Hello {username_value.lower()}, your feed is empty."
        assert driver.find_element(by=By.XPATH, value=".//strong").text == username_value.lower()
        self.log.info("Registration for user '%s' was success and verified", username_value)
