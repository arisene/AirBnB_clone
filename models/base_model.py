#!/usr/bin/python3
"""
BaseModel class 
defines all common attributes/methods
for other classes
"""
import uuid
from datetime import datetime


class BaseModel:
    
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        class_name = type(BaseModel).__name__
        return f"{class_name} ({self.id} {self.__dict__})"
    
    def save(self):
        self.updated_at = datetime.now()
    
    def to_dict(self):
        obj_dict = {}
        obj_dict.update(self.__dict__)
        obj_dict['__class__'] = self.__class__.__name__
        #convert into ISO formart
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()

        return obj_dict
        
        

