class MainView:

    def __init__(self):
        pass

    def view_main_menu(self):
        print("===== Bienvenue =====")
        print("Veuillez choisir une action")
        print("1. Gestion des tournois")
        print("2. Gestion des joeurs")
        print("3. Quitter")
        choice = input()
        return choice