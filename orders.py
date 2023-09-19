import requests
import configuration
import data


def create_order():
    return requests.post (configuration.URL + configuration.CREATE_ORDER, json=data.CREATE_ORDER_BODY)

def get_order_by_track(track):
    return requests.get (configuration.URL + configuration.GET_ORDER_BY_TRACK + 'track')

