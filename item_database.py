import requests
import json

BASE_URL = "http://services.runescape.com/m=itemdb_oldschool"

GET_ITEM_URL = "/api/catalogue/detail.json?item={0}"
GET_CATAGORY_URL = "/api/catalogue/items.json?category=1&alpha={0}&page={1}"
GET_HISTORIC_VALUE_URL = "/api/graph/{0}.json"


def build_api_call(FUNCTION_URL, itemID, **kwargs):
    """ Builds an api call from static URL's"""
    url = BASE_URL + FUNCTION_URL.format(itemID, kwargs)
    return url


def json_api_call(url):
    """ Send request to url """
    response = requests.get(url)
    return response.json()


def harvest(function, itemID, **kwargs):
    """ Takes in an action and an item, returns the appropriate json item data """
    try:
        payload = build_api_call(itemID, function, kwargs)
        response = json_api_call(payload)
    except Exception as e:
        return None

    return response


def getitem(itemID):
    """  Returns a JSON response of details about the item based on the ID. \
    Data includes: a small and large icon, the name, description, and price trends. """

    return harvest(GET_ITEM_URL, itemID)


def gethistory(itemID):
    """ Returns a JSON response of data to generate a graph for an item. \
    The data is in the format of "Epoch Time: Item Value" """

    return harvest(GET_HISTORIC_VALUE_URL, itemID)


def getcatagory(itemID, page=1):
    """  Returns a JSON response of details about a category of items on the website. \
    OSRS only supports one category on the website and thus is set to 1 on the endpoint. \

    itemID - The alphabetical letter that all items must start with in the results. Use "%23" to get items which start with a number.

    page - The page number to reference. There are 12 results per page.

    """

    if type(itemID) == int:
        itemID = "%23{0}".format(itemID)

    return harvest(GET_CATAGORY_URL, itemID, page)


def get_price_from_json(json):
    """ Returns the price nested in the json data as an integer """
    try:
        return int(json['current']['price'])
    except ValueError as e:
        return "NaN"


def get_image_from_json(json):
    """ Returns the image url nested in the json data"""
    pass


def item_name_to_id(item_name):
    """ Does a lookup in the item file, returning the appropriate ID for the given item"""
    pass


def create_example():
    """ Writes example json to "exchange_api_example.json """

    with open('exchange_api_example.json', 'w') as f:
        json.dump(getitem(2), f)


if __name__ == "__main__":
    """ Run Unit Test"""
    pass