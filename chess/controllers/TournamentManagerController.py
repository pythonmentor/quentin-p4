from views.TournamentManagerView import TournamentManagerView

class TournamentManagerController:

    def __init__(self):
        pass

    def get_input_tournament_manager(self):
        tournament_management = TournamentManagerView()
        management_choice = tournament_management.tournament_manager_view()

        if choice == "1":
            pass
        elif choice == "2":
            pass
        elif choice == "3":
                self.running = False