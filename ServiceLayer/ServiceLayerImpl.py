from abc import ABC, abstractmethod


class ServiceLayerImpl(ABC):

    def __init__(self, dao):
        assert isinstance(dao, object)
        self.dao = dao

    @abstractmethod
    def add_bookmark(self, bookmark):
        self.dao.add_bookmark(bookmark)

    @abstractmethod
    def view_bookmark_by_id(self, id):
        return self.dao.view_bookmark_by_id(id)

    @abstractmethod
    def view_all_bookmarks(self):
        return self.dao.view_all_bookmarks()
