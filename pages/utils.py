import random
import string


def random_num():
    """Generate random number"""
    return str(random.randint(111111, 999999))


def random_str(length=5):
    """Generate random string"""
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))


class User:

    def __init__(self, username="", email="", password=""):
        self.username = username if username else f"{random_str()}{random_num()}"
        self.email = email if email else f"{self.username}@mail.com"
        self.password = password if password else f"{random_str(7)}{random_num()}"
