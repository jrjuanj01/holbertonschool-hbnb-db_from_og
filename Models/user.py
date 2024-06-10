import uuid
from datetime import datetime
from .place import Place
from .review import Review
from Persistence.data_manager import DataManager


class User:
    """class that defines a user"""
    emails = []  # list of existing email addresses
    data_manager = DataManager()

    def __init__(self, first_name: str, last_name: str,
                 email: str, password: str):
        """initialize a user"""
        if email in User.emails:  # handle unique email
            raise ValueError("email not available")
        User.emails.append(email)
        self.__email = email
        self.__id = str(uuid.uuid4())
        self.__created_at = datetime.now().strftime("%B/%d/%Y %I:%M:%S %p")
        self.__updated_at = self.created_at
        self.__first_name = first_name
        self.__last_name = last_name
        self.__password = password
        self.places = []  # list of places owned by the user
        self.reviews = []  # list of reviews done by the user

    def add_place(self, place):
        """add place to user places"""
        if not isinstance(place, Place):
            raise ValueError("place must be a Place instance")
        self.places.append(place)
        place.host_id = self.__id
        place.host = self.__first_name + " " + self.__last_name
        self.__updated_at = datetime.now().strftime("%B/%d/%Y %I:%M:%S %p")

    def add_review(self, review):
        """add review to user reviews"""
        if not isinstance(review, Review):
            raise ValueError("review must be a Review instance")
        self.reviews.append(review)
        review.user_name = self.__first_name + " " + self.__last_name
        self.__updated_at = datetime.now().strftime("%B/%d/%Y %I:%M:%S %p")

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
    def first_name(self):
        """first name getter"""
        return self.__first_name

    @first_name.setter
    def first_name(self, name):
        """first name setter"""
        if type(name) is not str:
            raise TypeError("first name must be a text string")
        if not name or len(name.strip()) == 0:
            raise ValueError("first name cannot be empty")
        self.__first_name = name
        self.__updated_at = datetime.now().strftime("%B/%d/%Y %I:%M:%S %p")

    @property
    def last_name(self):
        """last name getter"""
        return self.__last_name

    @last_name.setter
    def last_name(self, name):
        """last name setter"""
        if type(name) is not str:
            raise TypeError("last name must be a text string")
        if not name or len(name.strip()) == 0:
            raise ValueError("last name cannot be empty")
        self.__last_name = name
        self.__updated_at = datetime.now().strftime("%B/%d/%Y %I:%M:%S %p")

    @property
    def email(self):
        """email getter"""
        return self.__email

    @email.setter
    def email(self, email):
        """email setter"""
        if type(email) is not str:
            raise TypeError("email must be a text string")
        if not email or len(email.strip()) == 0:
            raise ValueError("email cannot be empty")
        self.__email = email
        self.__updated_at = datetime.now().strftime("%B/%d/%Y %I:%M:%S %p")

    @property
    def password(self):
        """password getter"""
        return self.__password

    @password.setter
    def password(self, password):
        """password setter"""
        if type(password) is not str:
            raise TypeError("password must be a text string")
        if not password or len(password.strip()) == 0:
            raise ValueError("password cannot be empty")
        self.__password = password
        self.__updated_at = datetime.now().strftime("%B/%d/%Y %I:%M:%S %p")

    @classmethod
    def create(cls, first_name, last_name, email, password):
        """create new user"""
        user = cls(first_name, last_name, email, password)
        cls.data_manager.save(user)
        return user

    @classmethod
    def get(cls, user_id):
        """get user by id"""
        return cls.data_manager.get(user_id, "User")

    def update(self):
        """update user data"""
        self.data_manager.update(self)

    def delete(self):
        """delete user data"""
        self.data_manager.delete(self.id, "User")

    @classmethod
    def all(cls):
        """Retrieve all users"""
        return cls.data_manager.all("User")
