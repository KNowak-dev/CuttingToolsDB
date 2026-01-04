from enum import IntEnum
from tools_storage import ToolStorage
from edv_number import EDVNumber

class EditOption(IntEnum):
    TYPE_TOOL = 1
    ORIGIN = 2
    NR_EDV_SEMI_FINISHED_PRODUCT = 3
    KIND_TOOL = 4
    PRODUCTION_DETAIL = 5
    MACHINE = 6
    PRODUCTION_MACHINE = 7
    SEMI_FINISHED_PRODUCT_PRICE = 8
    TOTAL_PRICE = 9
    COATING = 10
    EXIT = 11

class EditOptionMenu:
    def show_main_menu(self):
        print("\nMenu główne")
        print("1. Typ narzędzia")
        print("2. Pochodzenie")
        print("3. EDV półfabrykatu")
        print("4. Rodzaj narzędzia")
        print("5. Detal produkcyjny")
        print("6. Maszyna")
        print("7. Maszyna produkcyjna")
        print("8. Cena półfabrykatu")
        print("9. Cena całkowita narzędzia")
        print("10. Powlekanie")
        print("11. Wyjdź")
    
    def get_choice(self):
        try:
            choice = EditOption(int(input("Wybierz opcję, którą chcesz edytować: ")))
            return choice
        except (ValueError, KeyError):
            print("Nieprawidłowy wybór. Spróbuj ponownie.")
            return None

class EditTool:
    def __init__(self, storage: ToolStorage):
        self.tools_storage = storage
        self.func_menu = EditOptionMenu()
       
    def start_edit_menu(self, tool):
        while True:
            self.func_menu.show_main_menu()
            if not self.execute(tool):
                break

    def SearchToolInStorageDB(self, edv: EDVNumber):
        tool = self.tools_storage.get(edv)
        if tool is None:
            raise KeyError("EDV nie znaleziony.")
        return tool

    def execute(self, tool):
        choice = self.func_menu.get_choice()
        if choice is None:
            return True

        if choice == EditOption.EXIT:
            return False

        if choice not in self.field_map:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")
            return True

        field_name = self.field_map[choice]
        current_value = getattr(tool, field_name)
        new_value_str = input(f"Wprowadź nową wartość dla {field_name} (aktualnie: {current_value}): ")

        try:
            if isinstance(current_value, int):
                new_value = int(new_value_str)
            elif isinstance(current_value, float):
                new_value = float(new_value_str)
            else:
                new_value = new_value_str
        except ValueError:
            print("Nieprawidłowy typ danych. Spróbuj ponownie.")
            return True

        setattr(tool, field_name, new_value)
        print(f"Pole {field_name} zostało zmienione na: {new_value}")
        return True

if __name__ == "__main__":
    pass
