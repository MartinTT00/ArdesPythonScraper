import pymongo
# TODO - add config


def init_client(connection_string):
    return pymongo.MongoClient(connection_string)
