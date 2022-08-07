import requests
import pytest


@pytest.mark.parametrize("image_number", [1, 2, 3])
def test_get_random_images(image_number):
    request = requests.get(f"https://dog.ceo/api/breeds/image/random/{image_number}")
    images = request.json()
    assert request.status_code == 200
    assert len(images["message"]) == image_number
    assert images["status"] == "success"


@pytest.mark.parametrize("breed,expected", [("hound", 7), ("bulldog", 3), ("bullterrier", 1)])
def test_get_breed(breed, expected):
    request = requests.get(f"https://dog.ceo/api/breed/{breed}/list/")
    breed = request.json()
    assert request.status_code == 200
    assert len(breed["message"]) == expected
    assert breed["status"] == "success"


@pytest.mark.parametrize("breed", ["akita", "husky", "malamute"])
def test_get_random_breed(breed):
    request = requests.get(f"https://dog.ceo/api/breed/{breed}/images/random")
    images = request.json()
    breed_name = images["message"].split("/")[-2]
    assert request.status_code == 200
    assert breed_name == breed
    assert images["status"] == "success"


def test_get_random_image():
    request = requests.get(f"https://dog.ceo/api/breeds/image/random/")
    images = request.json()
    assert request.status_code == 200
    assert images["message"][-3:] == "jpg"
    assert images["status"] == "success"


def test_get_all_breeds():
    breeds = requests.get("https://dog.ceo/api/breeds/list/all")
    assert breeds.status_code == 200
    assert len(breeds.json()["message"]) != 0
