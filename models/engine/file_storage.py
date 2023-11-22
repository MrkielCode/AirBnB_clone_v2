#!/usr/bin/python3
"""
This class represents a file strorage class

"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """ This class performs serialization and
    deserialiazation of an object

    Attributes:
        __file_path (str): name of file which objects are saved
        __objects (dict): a dictionary which class instance are
        converted to
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is None:
            return FileStorage.__objects

        filtered_objects = {}
        for obj_id, obj in self.__objects.items():
            if type(obj) == cls:
                filtered_objects[obj_id] = obj
        return filtered_objects

    def new(self, obj):
        """Set an object with key <obj class name>.id"""
        class_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(class_name, obj.id)] = obj

    def save(self):
        """ perform of serialization and save it to a json file """
        obj_dict = {}
        for key, value in FileStorage.__objects.items():
            obj_dict[key] = value.to_dict()

        with open(FileStorage.__file_path, "w") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """ perform deserialization of an object only if object exits"""
        try:
            with open(FileStorage.__file_path) as file:
                obj_dict = json.load(file)
                for value in obj_dict.values():
                    class_name = value["__class__"]
                    del value["__class__"]
                    obj = eval(class_name)(**value)
                    self.new(obj)
        except FileNotFoundError:
            return

    def delete(self, obj=None):
        """ delteting an __object if it existe """
        if obj is None:
            return

        key = f"{obj.__class__.__name__}.{obj.id}"
        if key in self.__objects:
            del self.__objects[key]
