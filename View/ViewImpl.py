from abc import ABC, abstractmethod

"""
    Abstract class and method that will hold
    the implementations of the view
"""


class ViewImpl(ABC):
    @abstractmethod
    def display(self, msg):
        print(msg)

    @abstractmethod
    def read(self, msg):
        return input(msg)
