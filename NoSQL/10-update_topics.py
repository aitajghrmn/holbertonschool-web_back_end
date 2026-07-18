#!/usr/bin/env python3
""" Function that changes all topics of a school document based on the name """
import pymongo


def update_topics(mongo_collection, name, topics):
    ''' update topics function
    '''
    query: dict = {'name': name}
    mongo_collection.update_many(query, {"$set": {"topics": topics}})
