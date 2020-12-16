from views.HomeView import HomeView
from models.Tournament import Tournament
from controllers.MainController import MainController

if __name__ == "__main__":
    vue = HomeView()
    controller = MainController()
    controller.get_choice_main_menu(vue)