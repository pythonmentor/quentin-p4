from views.MainView import MainView
from models.Tournament import Tournament

if __name__ == "__main__":
    start_menu = MainView()
    choice = start_menu.main_menu()
    tournois = Tournament()
    tournois.set_name("Python")
    print(tournois.name)
