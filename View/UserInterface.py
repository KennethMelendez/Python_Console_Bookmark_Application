from Dtos.Bookmark import Bookmark


class UserInterface:

    def __init__(self, io):
        assert isinstance(io, object)
        self.io = io

    def welcome_banner(self):
        self.io.display("Welcome To the Bookmark App")

    def user_prompt(self, msg):
        return self.io.read(msg)

    def display_msg(self, msg):
        self.io.display(msg)

    def menu(self):
        return ["Add Bookmark", "Remove Bookmark", "View Bookmark", "View All Bookmark", "Exit"]

    def main_menu(self):
        key = 1
        for option in self.menu():
            self.io.display(f"{key} {option}")
            key += 1

    def create_bookmark_prompt(self):
        title = self.user_prompt("Please Input Title.")
        description = self.user_prompt("Please Input Description.")
        url = self.user_prompt("Please Input URL")
        new_bookmark = Bookmark(title, description, url)
        self.display_msg("New Bookmark Added.")
        self.display_msg(new_bookmark.display_bookmark())

        return new_bookmark

    def display_all_bookmarks(self, bookmarks):
        for bookmark in bookmarks:
            self.io.display(f" IDno. [{bookmark.bookmark_id}] {bookmark.title} {bookmark.description} {bookmark.url}")
