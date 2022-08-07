import requests
import pytest


def test_get_posts():
    posts = requests.get("https://jsonplaceholder.typicode.com/posts")
    assert posts.status_code == 200
    assert len(posts.json()) != 0


@pytest.mark.parametrize("post_id", [1, 2, 3, 4, 5])
def test_get_post(post_id):
    post = requests.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}")
    assert post.status_code == 200
    assert post.json()["id"] == post_id


@pytest.mark.parametrize("post_id", [1, 2, 3, 4, 5])
def test_get_comments(post_id):
    comments = requests.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}/comments")
    assert comments.status_code == 200
    for comment in comments.json():
        assert comment["postId"] == post_id


def test_post_save():
    post_data = {
        "userId": 1,
        "title": "Привет",
        "body": "как дела",
    }
    post = requests.post("https://jsonplaceholder.typicode.com/posts", data=post_data)
    post = post.json()
    assert int(post["userId"]) == post_data["userId"]
    assert post["title"] == post_data["title"]
    assert post["body"] == post_data["body"]


def test_get_photos():
    photos = requests.get("https://jsonplaceholder.typicode.com/photos")
    assert photos.status_code == 200
    assert len(photos.json()) != 0
