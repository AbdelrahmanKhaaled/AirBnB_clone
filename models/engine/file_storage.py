#!/usr/bin/python3
'''File_Storage.'''
import os
import json
from models.base_model import BaseModel

class FileStorage:
    '''FileStorage Class.'''

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = obj.__class__.__name__ + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        with open(self.file_path, "a") as json_file:
            for obj in FileStorage.__objects:
                json.dump(obj, json_file)

    def reload(self):


