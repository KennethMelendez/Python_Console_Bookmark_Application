from View.View import View

io = View()


class UserInterface:

    def welcome_banner(self):
        io.display("Welcome To the Bookmark App")

    def user_prompt(self, msg):
        return io.read(msg)

    def display_msg(self, msg):
        io.display(msg)

    def menu(self):
        return ["Add Bookmark", "Remove Bookmark", "View Bookmark", "View All Bookmark", "Exit"]

    def main_menu(self):
        key = 1
        for option in self.menu():
            io.display(f"{key} {option}")
            key+=1

