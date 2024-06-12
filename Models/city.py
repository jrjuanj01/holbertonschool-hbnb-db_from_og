import uuid
from datetime import datetime
from Persistence.data_manager import DataManager


class City:
    """class that defines a city"""
    data_manager = DataManager()

    def __init__(self, name: str, country_code):
        """initialize a city"""
        self.__id = str(uuid.uuid4())
        self.__created_at = datetime.now().strftime("%B/%d/%Y %I:%M:%S %p")
        self.__updated_at = self.__created_at
        self.__name = name
        self.__country_code = country_code

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
    def country_code(self):
        """country getter"""
        return self.__country_code

    @country_code.setter
    def country_code(self, country_code):
        """country setter"""
        self.__country_code = country_code
        self.__updated_at = datetime.now().strftime("%B/%d/%Y %I:%M:%S %p")

    @classmethod
    def create(cls, name, country_code):
        """Create a new city"""
        city = cls(name, country_code)
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

    @classmethod
    def all(cls):
        """Retrieve all cities"""
        return cls.data_manager.all("City")

    def to_dict(self):
        """Return a dictionary representation of a city"""
        return {
            "id": self.__id,
            "created_at": self.__created_at,
            "updated_at": self.__updated_at,
            "name": self.__name,
            "country_code": self.__country_code
        }
