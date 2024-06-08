import uuid
from datetime import datetime
from ...Persistence.data_manager import DataManager


class City:
    """class that defines a city"""
    data_manager = DataManager()

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
        self.__updated_at = datetime.now().strftime("%B/%d/%Y %I:%M:%S %p")

    @property
    def country(self):
        """country getter"""
        return self.__country

    @country.setter
    def country(self, country):
        """country setter"""
        self.__country = country
        self.__updated_at = datetime.now().strftime("%B/%d/%Y %I:%M:%S %p")

    @classmethod
    def create(cls, name):
        """Create a new city"""
        city = cls(name)
        cls.data_manager.save(city)
        return city

    @classmethod
    def get(cls, city_id):
        """Get a specific city by ID"""
        return cls.data_manager.get(city_id, "City")

    def update(self):
        """Update city data"""
        self.data_manager.update(self)

    def delete(self):
        """Delete city"""
        self.data_manager.delete(self.id, "City")
