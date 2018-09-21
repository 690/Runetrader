import requests

BASE_URL = "http://services.runescape.com/m=itemdb_oldschool"
REQUEST_LIMIT_SECONDS = 50


def build_api_call(itemID):
    url = BASE_URL + "/api/catalogue/detail.json?item={0}".format(itemID)
    return url


def json_api_call(url):
    response = requests.get(url)
    return response.json()


def harvest(itemID):
    try:
        payload = build_api_call(itemID)
        response = json_api_call(payload)
    except Exception as e:
        return None

    return response  # 'RAW' refers to the non-prettified data of the cryptocompare api, hence the hardcore


print(harvest(2))