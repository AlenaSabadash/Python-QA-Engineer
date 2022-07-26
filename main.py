import csv
import json


def get_books():
    with open("./assets/books.csv", "r") as f:
        return list(csv.DictReader(f))


def get_users():
    with open("./assets/users.json", "r") as f:
        return json.load(f)


def save_result_file(chunks, users):
    for i, books in enumerate(chunks):
        users[i]["books"] = books

    with open("./assets/result.json", "w") as f:
        f.write(json.dumps(users))


def chunkify(lst, n):
    return [lst[i :: len(n)] for i in range(len(n))]


def main():
    books = get_books()
    users = get_users()
    chunks = chunkify(books, users)
    save_result_file(chunks, users)


if __name__ == "__main__":
    main()
