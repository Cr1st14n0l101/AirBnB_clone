#!/usr/bin/python3
"""Class FileStorage"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.review import Review
from models.state import State
from models.place import Place
from models.amenity import Amenity


class FileStorage:
    """Class FileStorage to store data"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return __objects kind dict"""
        return self.__objects

    def new(self, obj):
        """Create Key with class and id and add in __objects"""
        key = str(obj.to_dict()['__class__']) + "." + str(obj.to_dict()['id'])
        self.__objects[key] = obj

    def save(self):
        """save information type .json in a file (__file_path)"""
        new_dict = {}
        filename = str(self.__file_path)
        for key in self.__objects:
            new_dict[key] = self.__objects[key].to_dict()
        with open(filename, 'w') as f:
            json.dump(new_dict, f, indent=4)

    def reload(self):
        """reload information type .json of the file (__file_path)"""
        filename = str(self.__file_path)
        try:
            if os.path.exists(filename):
                with open(filename, 'r') as f:
                    dict_f = {}
                    read_line = f.read()
                    if read_line != "":
                        dict_f = json.loads(read_line)

                    for key, value in dict_f.items():
                        if key not in self.__objects.keys():
                            className = value["__class__"]
                            newInst = eval("{}(**value)".format(className))
                            self.new(newInst)
        except Exception:
            pass
