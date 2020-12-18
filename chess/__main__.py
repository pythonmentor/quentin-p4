from views.HomeView import HomeView
from models.Tournament import Tournament
from controllers.MainController import MainController

if __name__ == "__main__":
    home_view = HomeView()
    controller = MainController()
    controller.get_input_main_menu(home_view)