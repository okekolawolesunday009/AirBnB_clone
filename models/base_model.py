#!/usr/bin/python3
"""Defines a base class"""
import uuid
from datetime import datetime


class BaseModel:
    """class base doc"""
    def __init__(self, *args, **kwargs):
        """
        Update attributes using positional arguments.
        Args:
            args: Positional arguments in the order id, 
            craeted_at, updated_at, __class__.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'created_at':
                    dated = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    self.created_at = dated
                elif key == 'updated_at' or key == "created_at":
                    self.__dict__[key] = value
                    
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            from models import storage 
            storage.new(self)
            
    def __str__(self):
        """string documentation"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """time saved"""
        self.updated_at = datetime.now()
        from models import storage 
        storage.save()

    def to_dict(self):
        """Returns a dictionary representation of the instance."""
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict = self.__dict__.copy()
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict