import csv
import json
from dataclasses import dataclass, asdict


@dataclass
class UserDto:
    name: str
    gender: str
    address: str
    age: int
    books: list[dict]


def get_books():
    with open("./assets/books.csv", "r") as f:
        return list(csv.DictReader(f))


def get_users():
    with open("./assets/users.json", "r") as f:
        return json.load(f)


def save_result_file(chunks, users):
    users_result = []
    for i, books in enumerate(chunks):
        user = UserDto(
            name=users[i]["name"],
            gender=users[i]["gender"],
            address=users[i]["address"],
            age=users[i]["age"],
            books=books,
        )

        users_result.append(asdict(user))

    with open("./assets/result.json", "w") as f:
        f.write(json.dumps(users_result))


def chunkify(lst, n):
    return [lst[i :: len(n)] for i in range(len(n))]


def main():
    books = get_books()
    users = get_users()
    chunks = chunkify(books, users)
    save_result_file(chunks, users)


if __name__ == "__main__":
    main()
