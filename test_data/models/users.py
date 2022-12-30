import random
from pydantic import BaseModel, validator

admin_user = ("user", "bitnami")


class TestUser(BaseModel):
    first_name = "test-first_name"
    last_name = "test-last_name"
    email = "test@mail.com"
    telephone = "89999999999"
    password = "passwd"
    is_random_user = False

    @validator("is_random_user")
    def check_is_random_user(cls, v, values):
        if v:
            values.email = f"{values.email}{random.randint(0, 255)}"


def get_user():
    return admin_user


def get_customer(is_random_user=False):
    return TestUser(is_random_user=is_random_user)
