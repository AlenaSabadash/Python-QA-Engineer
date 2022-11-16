import random

_users = [
    ("user", "bitnami"),
]


def get_user():
    return random.choice(_users)
