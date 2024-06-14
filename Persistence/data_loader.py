import json
import os

DATA_FILE = "data.json"


def load_data():
    """Load data from data.json file"""
    
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            loaded_data = json.load(f)
            storage = {
                "User": {},
                "Place": {},
                "Review": {},
                "City": {},
                "Country": {},
                "Amenity": {}
            }
            objects = {}

            for data_type, items in loaded_data.items():
                for identifier, obj_data in items.items():
                    if data_type == "User":
                        from Models.user import User
                        obj = User.from_dict(obj_data)
                    elif data_type == "Place":
                        from Models.place import Place
                        obj = Place.from_dict(obj_data)
                    elif data_type == "Review":
                        from Models.review import Review
                        obj = Review.from_dict(obj_data)
                    elif data_type == "City":
                        from Models.city import City
                        obj = City.from_dict(obj_data)
                    elif data_type == "Amenity":
                        from Models.amenity import Amenity
                        obj = Amenity.from_dict(obj_data)

                    storage[data_type][identifier] = obj_data
                    objects[identifier] = obj

            return storage, objects
    return {
        "User": {},
        "Place": {},
        "Review": {},
        "City": {},
        "Country": {},
        "Amenity": {}
        }
