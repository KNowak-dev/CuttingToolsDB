
from enum import IntEnum
from tools_storage import ToolStorage
from edv_number import EDVNumber

class ToolOrigin(IntEnum):
    KUPNE = 1
    PRODUKOWANE = 2

class ChooseOrigin:
    def show_tool_origin_menu(self):
        print("\nPochodzenie narzędzia:")
        print("1. Kupne")
        print("2. Produkowane")

    def get_tool_origin(self):
        try:
            choice = int(input("Wybierz pochodzenie"))
            return choice
        except ValueError:
            print("Nieprawidłowy wybór")
            return None
        
class InputToolOrigin:
    def __init__(self, tool_storage: ToolStorage):
        self.origin_tool = ChooseOrigin()
        self.tool_storage = tool_storage
        self.selected_type: str = None

    def start_choose_origin(self):
        self.origin_tool.show_tool_origin_menu()
        choice = self.origin_tool.get_tool_origin()
        return self.execute(choice)
           
    def get_edv(self, edv: EDVNumber):
        tool = self.tool_storage.get(edv)
        if tool is None:
            raise KeyError("Edv is not found.")
        
        return tool

    def execute(self, choice):
        if choice is None:
            return None
        
        match choice:
            case ToolOrigin.KUPNE:
                self.selected_type = "Kupne"
                return self.selected_type
        
            case ToolOrigin.PRODUKOWANE:
                self.selected_type = "Produkowane"
                return self.selected_type
            
            case _:
                print("Nieprawidłowy wybór")
                return None
    
if __name__ == "__main__":
    pass
        

