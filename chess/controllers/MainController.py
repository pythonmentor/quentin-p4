from controllers.TournamentManagerController import TournamentManagerController

class MainController:

    def __init__(self):
        self.running = True

    def get_input_main_menu(self, home_view):
        choice = home_view.home_menu()
        
        while self.running:
            if choice == "1":
               tournament_management = TournamentManagerController()
               tournament_management.get_input_tournament_manager()
            elif choice == "2":
                pass
            elif choice == "3":
                self.running = False