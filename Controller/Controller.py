class Controller:

    def __init__(self, ui, sl):
        assert isinstance(ui, object)
        assert isinstance(sl, object)
        self.ui = ui
        self.sl = sl

    def run(self):
        try:
            self.ui.welcome_banner()
            start_program = True
            while start_program == True:
                self.ui.main_menu()
                user_response = self.user_prompt()
                self.display_user_response(user_response)

                # ADD BOOKMARK CODE
                if user_response == str(1):
                    self.add_bookmark()

                # REMOVE BOOKMARK
                if user_response == str(2):
                    self.remove_bookmark()

                # DISPLAY BOOKMARK CODE
                if user_response == str(3):
                    self.display_bookmark()

                # DISPLAY ALL BOOKMARKS CODE
                if user_response == str(4):
                    self.display_all_bookmarks()

                # END PROGRAM CODE
                if user_response == str(len(self.ui.menu())):
                    start_program = False
        except Exception:
            self.ui.error_message()

    def user_prompt(self):
        return self.ui.user_prompt("Please input response")

    def display_user_response(self, result):
        self.ui.display_msg(result)

    def add_bookmark(self):
        new_bookmark = self.ui.create_bookmark_prompt()
        self.sl.add_bookmark(new_bookmark)

    def display_all_bookmarks(self):
        self.ui.display_all_bookmarks(self.sl.view_all_bookmarks())

    def display_bookmark(self):
        bookmark_id = self.ui.prompt_id()
        bookmark = self.sl.view_bookmark_by_id(int(bookmark_id))
        self.ui.display_bookmark(bookmark)

    def remove_bookmark(self):
        bookmark_id = self.ui.prompt_id()
        self.sl.remove_bookmark_by_id(bookmark_id)
