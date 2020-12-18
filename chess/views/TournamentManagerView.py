class TournamentManagerView:

    def __init__(self):
        pass

    def tournament_manager_view(self):
        print("====== Gestion du tournois ======")
        print("Veuillez choisir une option ci dessous:")
        print("1. Créer un tournois")
        print("2. Afficher la liste des tournois")
        print("3. Retour")
        choice = input("Par exemple tapez '1' pour acceder à la gestion des tournois\n")
        return choice