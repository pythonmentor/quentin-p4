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
    
    def tournament_creation(self):
        print("====== Creation du tournois ======")
        return {
            "name": input("Entrez un nom:\n"),
            "location": input("Entrez un lieu:\n"),
            "start_date": input("Entrez une date de debut:\n"),
            "end_date": input("Entrez une date de fin:\n"),
            "times_control": input("Entrez le controle de temps:\n"),
            "description": input("Entrez une description:\n")
        }