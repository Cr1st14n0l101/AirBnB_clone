#!/usr/bin/python3
"""Module for class Base"""

import models
import uuid
import datetime

class BaseModel:
    """
    class BaseModel that defines all common attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """Contructor"""
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        setattr(self, key, datetime.datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()

    def __str__(self):
        """Return a string that represent the objects class"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the public instance attribute updated_at with the current datetime"""
        models.storage.new(self)
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__ of the instance"""
        new_dict = {}
        for key, value in self.__dict__.items():
            if type(value) is datetime.datetime:
                new_dict[key] = value.isoformat("T")
            else:
                new_dict[key] = value
        new_dict['__class__'] = self.__class__.__name__
        return new_dict


