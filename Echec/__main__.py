from views.MainView import MainView
from models.Tournament import Tournament
from controllers.MainController import MainController

if __name__ == "__main__":
    vue = MainView()
    controller = MainController()
    controller.get_choice_main_menu(vue)