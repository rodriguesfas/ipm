#!/usr/bin/env python
# -*- coding: utf-8 -*-

from config import database

from pymongo import MongoClient
from mongoengine import *


class ConnectMongoDB(object):

    def __init__(self):
        self.client = MongoClient(database.DB['hostname'], database.DB['port'])
        self.db = self.client[database.DB['database']]
        self.conn()

    def conn(self):
        return self.db

    def insert_document(self, collection_name, document):
        try:
            collection = self.db[collection_name]
            _id = collection.insert_one(document).inserted_id
            return _id
        except Exception as err:
            print(err)

    def select_document(self, collection_name, key):
        try:
            collection = self.db[collection_name]
            result = collection.find_one(key)
            if(result):
                return result
            else:
                return False
        except Exception as err:
            log.logging.error(err)
            return result

    def select_document_all_key(self, collection_name, key):
        try:
            collection = self.db[collection_name]
            result = collection.find(key)
            
            annotations = []
            
            for anotation in result:
                annotations.append(anotation)

            return annotations
        except Exception as err:
            log.logging.error(err)
            return result

    def select_document_all(self, collection_name):
        try:
            collection = self.db[collection_name]
            item = []

            for data in collection.find():
                item.append(
                    {
                        "id": data['_id'],
                        "name": data['name'],
                        "register": data['register']
                    }
                )

            return item
        except Exception as err:
            print(err)

    def update_document(self, collection_name, key, document):
        try:
            collection = self.db[collection_name]
            result = collection.update_one(key, document)
            return result
        except Exception as err:
            print(err)

    def delete_document(self, collection_name, key):
        try:
            collection = self.db[collection_name]
            result = collection.delete_one(key)
            return result
        except Exception as err:
            print(err)
