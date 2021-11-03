#!/usr/bin/python3
"""Class FileStorage"""

import json
import os
from models.base_model import BaseModel


class FileStorage:
    """Class FileStorage to store data"""
    __file_path = "file"
    __objects = {}

    def all(self):
        """Return __objects kind dict"""
        return FileStorage.__objects

    def new(self, obj):
        """Create Key with class and id and add in __objects"""
        key = str(obj.to_dict()['__class__']) + "." + str(obj.to_dict()['id'])
        FileStorage.__objects[key] = obj

    def save(self):
        """save information type .json in a file (__file_path)"""
        new_dict = {}
        filename = str(FileStorage.__file_path) + ".json"
        for key in FileStorage.__objects:
            new_dict[key] = FileStorage.__objects[key].to_dict()
        with open(filename, 'w') as f:
            json.dump(new_dict, f, indent=4)

    def reload(self):
        """reload information type .json of the file (__file_path)"""
        filename = str(FileStorage.__file_path) + ".json"
        try:
            with open(filename, 'r') as f:
                dict_f = {}
                read_line = f.read()
                if read_line != "":
                    dict_f = json.loads(read_line)

                for key, value in dict_f.items():
                    if key not in FileStorage.__objects.keys():
                        className = value["__class__"]
                        newInst = eval("{}(**value)".format(className))
                        self.new(newInst)
        except:
            pass