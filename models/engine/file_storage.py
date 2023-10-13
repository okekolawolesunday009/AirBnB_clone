#!/usr/bin/python3
"""Defines a base class for storage"""
import json
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.user import User

class FileStorage:
    """Class to serialize instances to JSON and deserialize JSON to instances."""

    __file_path = "file.json"
    __objects = {}
    
    class_dict = {
        "BaseModel": BaseModel,
        "User": User,
        "State" : State,
        "City" : City,
        "Place" : Place,
        "Amenity" : Amenity,
        "Review" : Review
        }

    @classmethod
    def all(self):
        """Returns the dictionary of all objects."""
        return self.__objects

    @classmethod
    def new(self, obj):
        """Sets a new object in __objects."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    @classmethod
    def save(self):
        """Serializes __objects to JSON and saves to file."""
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()

        with open(self.__file_path, 'w', encoding="UTF-8") as file:
            json.dump(serialized_objects, file)

    @classmethod
    def reload(self):
        """Deserializes JSON file to __objects."""
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, obj_data in data.items():
                    class_name = key.split('.')[0]
                    obj_class = self.class_dict.get(class_name)
                    if obj_class:
                        obj_instance = obj_class(**obj_data)
                        self.__objects[key] = obj_instance
        except FileNotFoundError:
            pass
