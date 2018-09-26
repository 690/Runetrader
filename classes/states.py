from trading import trader
import random
import json


def find_margins(client):
    items = json.load(open('./data/items.json', 'r'))

    items = [item for item in items if client.is_member == False and item['members'] == "false" or client.is_member == True]
    items = random.sample(items, 2)

    margins = [trader.find_margin(client.exchange, item['name']) for item in items]

    print(margins)

op_dict = {'find margins' : find_margins}


