#!/usr/bin/env python3
"""
A base model module for the airbnb project
"""
import uuid
from datetime import datetime
import copy
from . import storage


class BaseModel:
    """
    A BaseModel class part of the base model module
    for the hbnb project
    """
    def __init__(self, *args, **kwargs):
        """
        the init method to initialize our objects
        """
        self.id = str(uuid.uuid4())

        if kwargs:

            for key, value in kwargs.items():

                if key != '__class__':

                    if key == 'created_at' or key == 'updated_at':
                        setattr(self, key, datetime.fromisoformat(value))

                    else:
                        setattr(self, key, value)
        else:

            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        returns a string representation of the object
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        updates the object created from the class
        and saves the data/status to a file or any
        other storage system
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        returns the dictionary representation
        of the instance with the class name where it is
        derived added and created_at, updated_at atributes
        have been converted to iso format
        """
        dict_to_return = copy.deepcopy(self.__dict__)
        dict_to_return["__class__"] = self.__class__.__name__
        dict_to_return["created_at"] = self.created_at.isoformat()
        dict_to_return["updated_at"] = self.updated_at.isoformat()
        return dict_to_return
