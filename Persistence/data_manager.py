from .persistence_interface import IPersistenceManager


class DataManager(IPersistenceManager):
    """class that defines a data manager"""
    def __init__(self):
        """initialize a data manager"""
        self.storage = {
                        "User": {}, "Place": {},
                        "Review": {}, "City": {},
                        "Country": {}, "Amenity": {}
                        }

    def get(self, data_id, data_type):
        """get data"""
        return self.storage[data_type].get(data_id)

    def save(self, data):
        """save a data"""
        data_type = type(data).__name__
        # handle country cause it has no id
        self.storage[data_type][data.id] = data

    def update(self, data):
        """update data"""
        data_type = type(data).__name__
        if data.id in self.storage[data_type]:
            self.storage[data_type][data.id] = data
        else:
            raise ValueError(f"{data_type} with id {data.id} does not exist")

    def delete(self, data_id, data_type):
        """delete data"""
        if data_id in self.storage[data_type]:
            del self.storage[data_type][data_id]
        else:
            raise ValueError(f"{data_type} with id {data_id} does not exist")
