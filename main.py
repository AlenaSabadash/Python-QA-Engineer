import csv
import json
from dataclasses import dataclass, asdict, field


@dataclass
class BookDto:
    title: str
    author: str
    pages: int
    genre: str


@dataclass
class UserDto:
    name: str
    gender: str
    address: str
    age: int
    books: list[BookDto] = field(default_factory=list)


def get_books() -> list[BookDto]:
    with open("./assets/books.csv", "r") as f:
        books = list(csv.DictReader(f))
        return [
            BookDto(
                title=book["Title"],
                author=book["Author"],
                pages=int(book["Pages"]),
                genre=book["Genre"],
            )
            for book in books
        ]


def get_users() -> list[UserDto]:
    with open("./assets/users.json", "r") as f:
        users = json.load(f)
        return [
            UserDto(
                name=user["name"],
                gender=user["gender"],
                address=user["address"],
                age=user["age"],
            )
            for user in users
        ]


def save_result_file(books_chunks: list[list[BookDto]], users: list[UserDto]) -> None:
    users_result = []
    for i, books in enumerate(books_chunks):
        user = users[i]
        user.books = books

        users_result.append(asdict(user))

    with open("./assets/result.json", "w") as f:
        f.write(json.dumps(users_result))


def chunkify(books: list[BookDto], users: list[UserDto]) -> list[list[BookDto]]:
    return [books[i :: len(users)] for i in range(len(users))]


def main():
    books = get_books()
    users = get_users()
    books_chunks = chunkify(books, users)
    save_result_file(books_chunks, users)


if __name__ == "__main__":
    main()
