from enum import IntEnum

class AppMenu(IntEnum):
    CUTTING_TOOL = 1
    COATING = 2
    PRICE = 3
    STORAGE = 4
    EXIT = 5

class MainMenu:
    def show_main_menu(self):
        print("Menu główne\n")
        print("1. Narzędzia")
        print("2. Powlekanie")
        print("3. Cena")
        print("4. Magazyn")
        print("5. Wyjdź")

    def get_choice(self):
        try:
            return AppMenu(int(input("Wybierz opcję:")))
        except (ValueError, KeyError):
            return None
        
class AppManager:
    def __init__(self):
        self.main_menu = MainMenu()

    def start_app(self):
        while True:
            self.main_menu.show_main_menu()
            if not self.execute():
                break

    def show_menu(self):
        self.main_menu.show_main_menu()

    def execute(self):
        choice = self.main_menu.get_choice()

        match choice:
            case AppMenu.CUTTING_TOOL:
                pass
            case AppMenu.COATING:
                pass
            case AppMenu.PRICE:
                pass
            case AppMenu.STORAGE:
                pass
            case AppMenu.EXIT:
                return False
            case _:
                print("Nieprawidłowy wybór")
        return True
    
if __name__ == "__main__":
    app = AppManager()
    app.start_app()