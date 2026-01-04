from enum import IntEnum
from tools_storage import ToolStorage
from edv_number import EDVNumber

class ToolType(IntEnum):
    OBROTOWE = 1
    TOCZNE = 2

class ChooseType:
    def show_tool_type_menu(self):
        print("\nTyp narzędzia:")
        print("1. Obrotowe")
        print("2. Toczne")

    def get_type_tool(self):
        try:
            choice = int(input("Wybierz typ"))
            return choice
        except ValueError:
            print("Nieprawidłowy wybór")
            return None
        
class InputTypeTool:
    def __init__(self, tool_storage: ToolStorage):
        self.type_tool = ChooseType()
        self.tool_storage = tool_storage
        self.selected_type: str = None

    def start_choose_type(self):
        self.type_tool.show_tool_type_menu()
        choice = self.type_tool.get_type_tool()
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
            case ToolType.OBROTOWE:
                self.selected_type = "Obrotowe"
                return self.selected_type
        
            case ToolType.TOCZNE:
                self.selected_type = "Toczne"
                return self.selected_type
            
            case _:
                print("Nieprawidłowy wybór")
                return None
    
if __name__ == "__main__":
    pass
        
