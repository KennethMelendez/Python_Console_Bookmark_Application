from View.UserInterface import UserInterface

ui = UserInterface()


class Controller:
    def run(self):
        ui.welcome_banner()
        startProgram = True
        while startProgram == True:
            ui.main_menu()
            user_response = user_prompt()
            display_user_response(user_response)
            if user_response == str(len(ui.menu())):
                startProgram = False


def user_prompt():
    return ui.user_prompt("Please input response")


def display_user_response(result):
    ui.display_msg(result)
