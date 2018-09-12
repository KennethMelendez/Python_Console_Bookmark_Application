from Dao.DaoImpl import DaoImpl


class Dao(DaoImpl):
    def add_bookmark(self, bookmark):
        super().add_bookmark(bookmark)

    def view_bookmark_by_id(self, id):
        return super().view_bookmark_by_id(id)

    def view_all_bookmarks(self):
        return super().view_all_bookmarks()

    def remove_bookmark_by_id(self, bookmark_id):
        super().remove_bookmark_by_id(bookmark_id)