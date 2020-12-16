class MainController:

    def __init__(self):
        #self.vue = vue()
        pass

    def get_choice_main_menu(self, vue):
        choice = vue.home_menu()
        if choice == "1":
            print("choix 1")
        elif choice == "2":
            print("choix 2")
        elif choice == "3":
            print("choix 3")
