import json


def read_configs():
    with open('configs.json') as f:
        return json.load(f)


def get_trakt_username():
    return read_configs()['trakt']['username']


def get_trakt_client_id():
    return read_configs()['trakt']['client_id']


def get_trakt_client_secret():
    return read_configs()['trakt']['client_secret']
