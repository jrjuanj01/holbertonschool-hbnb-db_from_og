import uuid
from datetime import datetime
from Persistence.data_manager import DataManager


class Amenity:
    """class that defines an amenity"""
    data_manager = DataManager()

    def __init__(self, name: str):
        """initialize an amenity"""
        self.__id = str(uuid.uuid4())
        self.__created_at = datetime.now().strftime("%B/%d/%Y %I:%M:%S %p")
        self.__updated_at = self.__created_at
        self.__name = name

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

    @classmethod
    def create(cls, name):
        """Create a new amenity"""
        amenity = cls(name)
        cls.data_manager.save(amenity.id, "Amenity", amenity.to_dict())
        return amenity

    @classmethod
    def get(cls, amenity_id):
        """Get a specific amenity by ID"""
        return cls.data_manager.get(amenity_id, "Amenity")

    def update(self):
        """Update amenity data"""
        self.data_manager.update(self.id, "Amenity", self.to_dict())

    def delete(self):
        """Delete amenity"""
        self.data_manager.delete(self.id, "Amenity")

    @classmethod
    def all(cls):
        """retrieve all amenities"""
        return cls.data_manager.all("Amenity")

    def to_dict(self):
        """Return a dictionary representation of an amenity"""
        return {
            "id": self.__id,
            "created_at": self.__created_at,
            "updated_at": self.__updated_at,
            "name": self.__name,
        }
