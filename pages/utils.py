"""Useful functions and objects"""
import datetime
import logging
import random
import string
from time import sleep
from typing import Optional

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeDriver
from selenium.webdriver.firefox.webdriver import WebDriver as MozilaDriver

from constants.base import BaseConstants
from constants.create_post_page import CreatePostPageConstants
from constants.text_presets import EN_TEXT, UA_TEXT


def random_num():
    """Generate random number"""
    return str(random.randint(111111, 999999))


def random_str(length=5):
    """Generate random string"""
    return "".join(random.choice(string.ascii_letters) for _ in range(length))


def wait_until_ok(timeout=5, period=0.25):
    """Retries function until ok"""
    logger = logging.getLogger("[WaitUntilOk]")

    def decorator(original_function):
        def wrapper(*args, **kwargs):
            end_time = datetime.datetime.now() + datetime.timedelta(
                seconds=timeout
            )
            while True:
                try:
                    return original_function(*args, **kwargs)
                # pylint: disable=broad-except
                except Exception as err:
                    if datetime.datetime.now() > end_time:
                        logger.warning("Catch: %s", err)
                        raise err
                    sleep(period)

        return wrapper

    return decorator


def log_wrapper(func):
    """Add logs for method using docsting"""

    def wrapper(*args, **kwargs):
        log = logging.getLogger("[LogDecorator]")
        result = func(*args, **kwargs)
        log.info(func.__doc__)
        return result

    return wrapper


def time_out_wrapper(func):
    """Handle TimeoutException"""

    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except TimeoutException:
            element_xpath = kwargs["xpath"] if kwargs.get("xpath") else args[1]
            # pylint: disable=raise-missing-from
            raise TimeoutException(f"Cannot find element '{element_xpath}'")
        return result

    return wrapper


class User:
    """Describes user"""

    def __init__(
            self,
            username: Optional[str] = "",
            email: Optional[str] = "",
            password: Optional[str] = "",
    ):
        self.username = username
        self.email = email
        self.password = password
        self.posts = []

    def fill_properties(self):
        """Generate random values for user fields"""
        variety = random_num()
        self.username = f"{random_str()}{variety}"
        self.email = f"{self.username}@mail.com"
        self.password = f"PassWord{variety}"


class Post:
    """Describes post"""

    def __init__(
            self,
            title: str = "",
            text: str = "",
            share_option: str = CreatePostPageConstants.SHARE_OPTION_ALL_USERS,
    ):
        self.title = title
        self.text = text
        self.share_option = share_option

    def fill_properties(self):
        """Generate random post with default values"""
        self.title = f"{random_str()}-{random_num()}"
        self.text = random_text(30, UA_TEXT)


def create_driver(browser: str):
    """Create driver driver according to provided browser"""
    if browser == BaseConstants.CHROME:
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        driver = ChromeDriver(options=options)
    elif browser == BaseConstants.FIREFOX:
        options = webdriver.firefox.webdriver.Options()
        options.add_argument("--headless")
        driver = MozilaDriver(options=options)
    else:
        raise ValueError(f"Unknown browser name: '{browser}'")
    driver.implicitly_wait(1)
    driver.get(BaseConstants.BASE_URL)
    return driver


def random_text(length=15, preset=EN_TEXT):
    """Create tests using provided sample"""
    words = preset.split(" ")
    return " ".join(
        random.choice(words).replace("\n", "") for _ in range(length)
    )
