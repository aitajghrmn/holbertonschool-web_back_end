#!/usr/bin/env python3
'''Python function that lists all documents in a collection
'''
import pymongo


def list_all(mongo_collection) -> list:
    ''' List all documents
    '''
    collections: list = []
    for doc in mongo_collection.find():
        collections.append(doc)
    return collections
