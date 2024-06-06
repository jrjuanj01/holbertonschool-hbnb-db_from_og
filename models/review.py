import uuid
from datetime import datetime


class Review:
    """class that defines a review"""
    def __init__(self, user_id, place_id, text, rating: int):
        """initialize a review"""
        self.__id = str(uuid.uuid4())
        self.__created_at = datetime.now().strftime("%B/%d/%Y %I:%M:%S %p")
        self.__updated_at = self.__created_at
        self.__user_id = user_id
        self.__user_name = None
        self.__place_id = place_id
        self.__text = text
        self.__rating = rating

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
    def user_id(self):
        """user id getter"""
        return self.__user_id

    @property
    def user_name(self):
        """user name getter"""
        return self.__user_name

    @user_name.setter
    def user_name(self, user_name):
        """user name setter"""
        self.__user_name = user_name
        self.__updated_at = datetime.now().strftime("%B/%d/%Y %I:%M:%S %p")

    @property
    def place_id(self):
        """place id getter"""
        return self.__place_id

    @property
    def text(self):
        """text getter"""
        return self.__text

    @text.setter
    def text(self, text):
        """text setter"""
        if type(text) is not str:
            raise TypeError("text must be a valid string")
        if not text or len(text.strip()) == 0:
            raise ValueError("text cannot be empty")
        self.__updated_at = datetime.now().strftime("%B/%d/%Y %I:%M:%S %p")

    @property
    def rating(self):
        """rating getter"""
        return self.__rating
    
    @rating.setter
    def rating(self, rating):
        """rating setter"""
        if type(rating) is not int:
            raise TypeError("rating must be an integer")
        if rating < 0 or rating > 5:
            raise ValueError("rating must be between 0 and 5")
        self.__updated_at = datetime.now().strftime("%B/%d/%Y %I:%M:%S %p")
