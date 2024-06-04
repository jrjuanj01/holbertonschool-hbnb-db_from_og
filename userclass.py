#!/usr/bin/python3
"""User Class"""
Master = __import__("master").Master


class User(Master):
    """class defining HBnB users"""

    def __init__(self, first_name, last_name, email, password):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__password = password
        self.created_at = super().creation().strftime("%B/%d/%Y %I:%M:%S %p")
        self.updated_at = self.created_at
        self.__id = super().uniqueid()

    @property
    def first_name(self):
        """first name getter"""
        return self.__first_name

    @first_name.setter
    def first_name(self, name):
        """first name setter"""
        self.__first_name = name
        self.updated_at = super().updated().strftime("%B/%d/%Y %I:%M:%S %p")

    @property
    def last_name(self):
        """last name getter"""
        return self.__last_name

    @last_name.setter
    def last_name(self, name):
        """last name setter"""
        self.__last_name = name
        self.updated_at = super().updated().strftime("%B/%d/%Y %I:%M:%S %p")

    @property
    def email(self):
        """email getter"""
        return self.__email

    @email.setter
    def email(self, email):
        """email setter"""
        self.__email = email
        self.updated_at = super().updated().strftime("%B/%d/%Y %I:%M:%S %p")

    @property
    def password(self):
        """password getter"""
        return self.__password

    @password.setter
    def password(self, password):
        """password setter"""
        self.__password = password
        self.updated_at = super().updated().strftime("%B/%d/%Y %I:%M:%S %p")
