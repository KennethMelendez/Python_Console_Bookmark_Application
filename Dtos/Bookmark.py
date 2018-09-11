class Bookmark:
    def __init__(self, title, description, url):
        self.title = title
        self.description = description
        self.url = url

    def display_bookmark(self):
        return f"Bookmark Title : {self.title} Description : {self.description} URL : {self.url}"


