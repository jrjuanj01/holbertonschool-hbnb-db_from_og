#!/usr/bin/python3
"""Place Class"""
Master = __import__("master").Master


class Place(Master):
    """class that defines an HBnB Place"""

    def __init__(self, name, description, address, city, host, rooms,
                 bathrooms, price, maxguests, amenities):  # add reviews
        self.__name = name
        self.__description = description
        self.__address = address
        self.__city = city
        self.__host = host
        self.__rooms = rooms
        self.__bathrooms = bathrooms
        self.__price = price
        self.__maxguests = maxguests
        self.__amenities = amenities
        self.created_at = super().creation().strftime("%B/%d/%Y %I:%M:%S %p")
        self.updated_at = self.created_at
        self.__id = super().uniqueid()
        # self.reviews = reviews (deal with assigning reviews)

    @property
    def name(self):
        """name getter"""
        return self.__name

    @name.setter
    def name(self, name):
        """name setter"""
        self.__name = name
        self.updated_at = super().updated().strftime("%B/%d/%Y %I:%M:%S %p")

    @property
    def description(self):
        """description getter"""
        return self.__description

    @description.setter
    def description(self, description):
        """description setter"""
        self.__description = description
        self.updated_at = super().updated().strftime("%B/%d/%Y %I:%M:%S %p")

    @property
    def address(self):
        """address getter"""
        return self.__address

    @address.setter
    def address(self, address):
        """address setter"""
        self.__address = address
        self.updated_at = super().updated().strftime("%B/%d/%Y %I:%M:%S %p")

    @property
    def city(self):
        """city getter"""
        return self.__city

    @city.setter
    def city(self, city):
        """city setter"""
        self.__city = city
        self.updated_at = super().updated().strftime("%B/%d/%Y %I:%M:%S %p")

    @property
    def host(self):
        """host getter"""
        return self.__host

    @host.setter
    def host(self, host):
        """host setter"""
        self.__host = host
        self.updated_at = super().updated().strftime("%B/%d/%Y %I:%M:%S %p")

    @property
    def rooms(self):
        """rooms getter"""
        return self.__rooms

    @rooms.setter
    def rooms(self, rooms):
        """rooms setter"""
        self.__rooms = rooms
        self.updated_at = super().updated().strftime("%B/%d/%Y %I:%M:%S %p")

    @property
    def bathrooms(self):
        """bathrooms getter"""
        return self.__bathrooms

    @bathrooms.setter
    def bathrooms(self, bathrooms):
        """bathrooms setter"""
        self.__bathrooms = bathrooms
        self.updated_at = super().updated().strftime("%B/%d/%Y %I:%M:%S %p")

    @property
    def price(self):
        """price getter"""
        return self.__price

    @price.setter
    def price(self, price):
        """price setter"""
        self.__price = price
        self.updated_at = super().updated().strftime("%B/%d/%Y %I:%M:%S %p")

    @property
    def maxguests(self):
        """maxguests getter"""
        return self.__maxguests

    @maxguests.setter
    def maxguests(self, maxguests):
        """maxguests setter"""
        self.__maxguests = maxguests
        self.updated_at = super().updated().strftime("%B/%d/%Y %I:%M:%S %p")

    @property
    def amenities(self):
        """amenities getter"""
        return self.__amenities

    @amenities.setter
    def amenities(self, amenities):
        """amenities setter"""
        self.__amenities = amenities
        self.updated_at = super().updated().strftime("%B/%d/%Y %I:%M:%S %p")
