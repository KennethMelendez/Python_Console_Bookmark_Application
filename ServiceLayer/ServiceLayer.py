from ServiceLayer.ServiceLayerImpl import ServiceLayerImpl


class ServiceLayer(ServiceLayerImpl):

    def add_bookmark(self, bookmark):
        super().add_bookmark(bookmark)

    def view_bookmark_by_id(self, id):
        super().view_bookmark_by_id(id)

    def view_all_bookmarks(self):
        return super().view_all_bookmarks()