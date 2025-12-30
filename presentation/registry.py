from enum import IntEnum

class MenuRegistration(IntEnum):

    SIGN_IN = 1
    CREATE_ACCOUNT = 2
    EXIT = 3

class Account:
    def __init__(self, login: str, password: str):
        self.login = login
        self.password = password

    def __str__(self):
        return f'Użytkownik: {self.login}.'
    
class Menu:
    def show(self):
        print("--- Okno logowania ---\n")
        print("1. Zaloguj się")
        print("2. Utwórz konto")

    def get_choice(self):
        try:
            return MenuRegistration(int(input("Wybierz opcję: ")))
        except (ValueError, KeyError):
            return None

class New_User:
    def __init__(self, users):
        self.users = users

    def add_user(self):
        login = input("Wprowadź login: ")

        for user in self.users:
            if user.login == login:
                print("Użytkownik już istnieje!")
                return

        password = input("Wprowadź hasło: ")
        self.users.append(SignIn(login, password))
        print(f"Pomyślnie dodano użytkownika {login}.")  

class Exist_User:
    def __init__(self, users):
        self.users = users
            
    def log_user(self):
        login = input("Wprowadź login: ")

        for user in self.users:
            if user.login == login:
                password = input("Wprowadź hasło: ")
                if user.password == password:
                    print(f'Użytkownik: {login} został pomyślnie zalogowany')
                else:
                    print("Wprowadzono błędne hasło.")
                return
        print("Użytkownik nie istnieje.")

class Manager:
    def __init__(self):
    
        self.menu = Menu()
        self.users = []
        self.exist_user = Exist_User(self.users)
        self.new_user = New_User(self.users)
        
    def start(self):

        while True:
            self.menu.show()
            if not self.execute():
                break
    
    def show_menu(self):
        self.menu.show()

    def execute(self):
        choice = self.menu.get_choice()

        match choice:
            case MenuRegistration.SIGN_IN:
                self.exist_user.log_user()
            case MenuRegistration.CREATE_ACCOUNT:
                self.new_user.add_user()
            case MenuRegistration.EXIT:
                print("Zamykanie okna logowania...")
                return False
            case _: 
                print("Nieprawidłowy wybór.")

        return True
    
if __name__ == "__main__":
    Manager().start()
