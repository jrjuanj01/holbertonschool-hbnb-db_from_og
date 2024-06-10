from .city import City
from Persistence.data_manager import DataManager


class Country:
    """class that defines a country"""
    countries = []  # list of existing countries
    data_manager = DataManager()

    def __init__(self, name):
        """initialize a country"""
        if name in Country.countries:
            raise ValueError("country already defined")
        self.__name = name
        self.cities = []

    def add_city(self, city):
        """add a city to the country"""
        if not isinstance(city, City):
            raise TypeError("city must be an instance of City")
        self.cities.append(city)

    @property
    def name(self):
        """name getter"""
        return self.__name

    @name.setter
    def name(self, name):
        """name setter"""
        if not name or len(name.strip()) == 0:
            raise ValueError("name cannot be empty")
        self.__name = name

    @classmethod
    def create(cls, name):
        """Create a new country"""
        country = cls(name)
        cls.data_manager.save(country)
        return country

    @classmethod
    def get(cls, name):
        """Get a specific country by name"""
        return cls.data_manager.get(name, "Country")

    def update(self):
        """Update country data"""
        self.data_manager.update(self)

    def delete(self):
        """Delete country"""
        self.data_manager.delete(self.__name, "Country")

    @classmethod
    def all(cls):
        """Retrieve all countries"""
        return cls.data_manager.all("Country")
