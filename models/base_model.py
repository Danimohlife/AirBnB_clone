#!/usr/bin/python3
"""
This module defines the BaseModel class which serves as a foundation
for other classes by providing common attributes and methods like
unique ID generation, timestamp handling, string representation,
serialization to dictionary, and update tracking.
"""

import uuid
from datetime import datetime


class BaseModel:
    """
    BaseModel defines all common attributes and methods
    that will be inherited by other classes.
    """

    def __init__(self):
        """
        Initializes a new instance of BaseModel with a unique ID,
        and timestamps for creation and last update.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """
        Returns a string representation of the instance in the format:
        [<class name>] (<self.id>) <self.__dict__>
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the `updated_at` timestamp to the current datetime.
        Should be called whenever the object is modified.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all attributes of the instance.
        Includes the class name under `__class__` and converts datetime
        attributes to ISO 8601 string format.
        """
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict
