from .persistence_interface import IPersistenceManager


class DataManager(IPersistenceManager):
    """class that defines a data manager"""
    def __init__(self):
        """initialize a data manager"""
        self.storage = {
                        "User": {}, "Place": {}, "Review": {},
                        "City": {}, "Amenity": {}
                        }

    def get(self, identifier, data_type):
        """get data with identifier. (name for country and id for others)"""
        if data_type not in self.storage:
            raise ValueError(f"Unsupported data type: {data_type}")
        return self.storage[data_type].get(identifier)

    def save(self, data):
        """save a data"""
        data_type = type(data).__name__
        if data_type not in self.storage:
            raise ValueError(f"Unsupported data type: {data_type}")
        self.storage[data_type][data.id] = data

    def update(self, data):
        """update data"""
        data_type = type(data).__name__
        if data_type not in self.storage:
            raise ValueError(f"Unsupported data type: {data_type}")
        if data.id in self.storage[data_type]:
            self.storage[data_type][data.id] = data
        else:
            raise ValueError(f"{data_type} '{data.id}' does not exist")

    def delete(self, identifier, data_type):
        """delete data with identifier. (name for country and id for others)"""
        if data_type not in self.storage:
            raise ValueError(f"Unsupported data type: {data_type}")
        if identifier in self.storage[data_type]:
            del self.storage[data_type][identifier]
        else:
            raise ValueError(f"{data_type} '{identifier}' does not exist")

    def all(self, data_type):
        """retrieve all data of a certain type"""
        if data_type not in self.storage:
            raise ValueError(f"Unsupported data type: {data_type}")
        return list(self.storage[data_type].values())
