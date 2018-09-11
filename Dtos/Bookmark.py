class Bookmark:

    def __init__(self, title, description, url):
        self.title = title
        self.description = description
        self.url = url
        self.bookmark_id = 0

    def display_bookmark(self):
        return f"Bookmark Title : {self.title} Description : {self.description} URL : {self.url}"
