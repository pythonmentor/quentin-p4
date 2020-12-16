class MainView:
    
    def __init__(self):
        pass

    def main_menu(self):
        print("====== Bienvenue ======")
        print("Veuillez choisir une option ci dessous:")
        print("1. Gestion des tournois")
        print("2. Gestion des joeurs")
        print("3. Quitter")
        choice = input("Par exemple tapez '1' pour acceder à la gestion des tournois\n")
        return choice