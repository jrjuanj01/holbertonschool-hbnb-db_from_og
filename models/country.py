class Country:
    """class that defines a country"""
    def __init__(self, name):
        """initialize a country"""
        self.__name = name

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
