#!/usr/bin/python3
"""Defines a base class for storage"""
import json


class FileStorage:
    """Class to serialize instances to JSON and deserialize JSON to instances."""

    __file_path = "file.json"
    __objects = {}

    @classmethod
    def all(cls):
        """Returns the dictionary of all objects."""
        return cls.__objects

    @classmethod
    def new(cls, obj):
        """Sets a new object in __objects."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        cls.__objects[key] = obj

    @classmethod
    def save(cls):
        """Serializes __objects to JSON and saves to file."""
        serialized_objects = {}

        print('save triggered')
        for key, obj in cls.__objects.items():
            print(obj)
            serialized_objects[key] = obj.to_dict()

        with open(cls.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    @classmethod
    def reload(cls):
        """Deserializes JSON file to __objects."""
        try:
            with open(cls.__file_path, 'r') as file:
                data = json.load(file)
                for key, obj_data in data.items():
                    class_name, obj_id = key.split('.')
                    cls_name = eval(class_name)
                    obj_instance = cls_name(**obj_data)
                    cls.__objects[key] = obj_instance
        except FileNotFoundError:
            pass
