import uuid
from datetime import datetime


class City:
    """class that defines a city"""
    def __init__(self, name: str):
        """initialize a city"""
        self.__id = str(uuid.uuid4())
        self.__created_at = datetime.now().strftime("%B/%d/%Y %I:%M:%S %p")
        self.__updated_at = self.__created_at
        self.__name = name
        self.__country = None

    @property
    def id(self):
        """id getter"""
        return self.__id

    @property
    def created_at(self):
        """creation datetime getter"""
        return self.__created_at

    @property
    def updated_at(self):
        """last update datetime getter"""
        return self.__updated_at

    @property
    def name(self):
        """name getter"""
        return self.__name

    @name.setter
    def name(self, name):
        """name setter"""
        if type(name) is not str:
            raise TypeError("name must be a text string")
        if not name or len(name.strip()) == 0:
            raise ValueError("name cannot be empty")
        self.__name = name
        self.updated_at = datetime.now().strftime("%B/%d/%Y %I:%M:%S %p")

    @property
    def country(self):
        """country getter"""
        return self.__country

    @country.setter
    def country(self, country):
        """country setter"""
        self.__country = country
        self.updated_at = datetime.now().strftime("%B/%d/%Y %I:%M:%S %p")
