import uuid
from datetime import datetime
from Persistence.data_manager import DataManager


class Review:
    """class that defines a review"""
    data_manager = DataManager()

    def __init__(self, user_id: str, place_id, comment: str, rating: int):
        """initialize a review"""
        self.__id = str(uuid.uuid4())
        self.__created_at = datetime.now().strftime("%B/%d/%Y %I:%M:%S %p")
        self.__updated_at = self.__created_at
        self.__user_id = user_id
        self.__place_id = place_id
        self.__comment = comment
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
    def place_id(self):
        """place id getter"""
        return self.__place_id

    @property
    def comment(self):
        """comment getter"""
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        """comment setter"""
        if type(comment) is not str:
            raise TypeError("comment must be a valid string")
        if not comment or len(comment.strip()) == 0:
            raise ValueError("comment cannot be empty")
        self.__updated_at = datetime.now().strftime("%B/%d/%Y %I:%M:%S %p")

    @property
    def rating(self):
        """rating getter"""
        return self.__rating

    @rating.setter
    def rating(self, rating: int):
        """rating setter"""
        if type(rating) is not int:
            raise TypeError("rating must be an integer")
        if rating < 1 or rating > 5:
            raise ValueError("rating must be between 1 and 5")
        self.__updated_at = datetime.now().strftime("%B/%d/%Y %I:%M:%S %p")

    @classmethod
    def create(cls, user_id, place_id, rating, comment):
        """create new review"""
        review = cls(user_id, place_id, rating, comment)
        cls.data_manager.save(review)
        return review

    @classmethod
    def get(cls, review_id):
        """get review by id"""
        return cls.data_manager.get(review_id, "Review")

    def update(self):
        """update review data"""
        self.data_manager.update(self)

    def delete(self):
        """delete review data"""
        self.data_manager.delete(self.id, "Review")

    @classmethod
    def all(cls):
        """Retrieve all users"""
        return cls.data_manager.all("Review")

    def to_dict(self):
        """convert review to dict"""
        return {
            "id": self.__id,
            "created_at": self.__created_at,
            "updated_at": self.__updated_at,
            "user_id": self.__user_id,
            "user_name": self.__user_name,
            "place_id": self.__place_id,
            "comment": self.__comment,
            "rating": self.__rating,
        }
