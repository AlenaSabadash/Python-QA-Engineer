import requests
import pytest


@pytest.mark.parametrize("per_page", [1, 2, 3])
def test_get_breweries(per_page):
    breweries = requests.get(f"https://api.openbrewerydb.org/breweries?per_page={per_page}")
    assert breweries.status_code == 200
    assert len(breweries.json()) == per_page


@pytest.mark.parametrize("by_city", ["San Diego", "Fayetteville", "Windsor"])
def test_get_breweries_by_city(by_city):
    breweries = requests.get(f"https://api.openbrewerydb.org/breweries?by_city=san_diego={by_city}")
    assert breweries.status_code == 200
    for brewery in breweries.json():
        assert brewery["city"] == by_city


def test_get_random_breweries():
    response = requests.get(f"https://api.openbrewerydb.org/breweries/random")
    breweries = response.json()
    assert response.status_code == 200
    assert len(breweries) == 1
    assert "name" in breweries[0]


@pytest.mark.parametrize(
    "by_name",
    [
        "3cross Fermentation Cooperative",
        "4th Tap Brewing Cooperative",
        "Broken Clock Brewing Cooperativ",
    ],
)
def test_get_breweries_by_name(by_name):
    breweries_name = requests.get(f"https://api.openbrewerydb.org/breweries?by_city=san_diego={by_name}")
    assert breweries_name.status_code == 200
    for brewery_name in breweries_name.json():
        assert brewery_name["name"] == by_name


@pytest.mark.parametrize(
    "brewery_id",
    [
        "banjo-brewing-fayetteville",
        "barrel-brothers-brewing-company-windsor",
        "bay-brewing-company-miami",
    ],
)
def test_get_single_brewery(brewery_id):
    brewery = requests.get(f"https://api.openbrewerydb.org/breweries/{brewery_id}")
    assert brewery.status_code == 200
    assert brewery.json()["id"] == brewery_id
