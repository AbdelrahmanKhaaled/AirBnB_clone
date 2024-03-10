#!/usr/bin/python3
'''Module for BaseModel Class'''
import uuid
from datetime import datetime
import json


class BaseModel():
    '''BaseModel Class.'''

    def __init__(self, *args, **kwargs):
        '''Constractor.'''
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif  key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()

    def __str__(self):
        '''returns data'''
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        ''' Update data.'''
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        ''' change to dictinary.'''
        inst_dict = self.__dict__.copy()
        inst_dict["__class__"] = self.__class__.__name__
        inst_dict["created_at"] = self.created_at.isoformat()
        inst_dict["updated_at"] = self.updated_at.isoformat()

        return inst_dict
