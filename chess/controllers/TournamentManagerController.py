from views.TournamentManagerView import TournamentManagerView

class TournamentManagerController:

    def __init__(self):
        pass

    def get_input_tournament_manager(self):
        tournament_management = TournamentManagerView()
        management_choice = tournament_management.tournament_manager_view()

        if management_choice == "1":
            new_tournament = tournament_management.tournament_creation()
            if type(new_tournament["name"]) == int:
                print("Good Job")
            else:
                print("nul")
        elif management_choice == "2":
            pass
        elif management_choice == "3":
            pass

        exit()