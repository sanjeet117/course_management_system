from abc import ABC, abstractmethod


class User(ABC):

    total_users = 0

    def __init__(self, user_id, name, email):
        self.__user_id = user_id
        self.__name = name
        self.__email = email

        User.total_users += 1

    @property
    def user_id(self):
        return self.__user_id

    @property
    def name(self):
        return self.__name

    @property
    def email(self):
        return self.__email

    @abstractmethod
    def display_profile(self):
        pass

    @classmethod
    def get_total_users(cls):
        return cls.total_users