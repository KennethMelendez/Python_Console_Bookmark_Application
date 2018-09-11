from abc import ABC, abstractmethod


class DaoImpl(ABC):

    def __init__(self):
        self.database = {}
        self.bookmark_id = 0

    @abstractmethod
    def add_bookmark(self, bookmark):
        self.bookmark_id = self.bookmark_id + 1
        assert (bookmark, object)
        bookmark.bookmark_id = self.bookmark_id
        self.database[self.bookmark_id] = bookmark

    @abstractmethod
    def view_bookmark_by_id(self, id):
        assert (id, int)
        return self.database.get(id)

    @abstractmethod
    def view_all_bookmarks(self):
        return list(self.database.values())
