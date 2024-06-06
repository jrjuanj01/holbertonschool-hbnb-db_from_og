from .city import City


class Country:
    """class that defines a country"""
    countries = []  # list of existing countries

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
