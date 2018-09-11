from View.ViewImpl import ViewImpl

"""
    View subclass| think of Interface in java
    that takes in the implementation of the viewimpl
"""


class View(ViewImpl):
    def display(self, msg):
        super().display(msg)

    def read(self, msg):
        return super().read(msg)
