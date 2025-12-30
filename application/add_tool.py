from dataclasses import dataclass
from tools_storage import ToolStorage
from user_input import user_input

@dataclass
class CuttingTool:
        nr_edv: str = ""
        type_tool: str = ""
        origin: str = ""
        nr_edv_semi_finished_product: str = ""
        kind_tool: str = ""
        production_detail: str = ""
        machine: str = ""
        production_machine: str = ""
        semi_finished_product_price: float = 0.0
        total_price: float = 0.0

class AddCuttingTool:
    def __init__(self, storage: ToolStorage):
        self.tool_storage = storage

    def add_tool(self, tool_data: CuttingTool): 
        self.tool_storage.storage.append(tool_data)
        print("Narzędzie dodane!")
        

if __name__ == "__main__":
    from user_input import (
        data_to_AddCuttingTool, Input_EDVNumber, Input_type_tool, Input_origin, 
        Input_semi_edv_number, Input_kind_tool, Input_prod_detail, 
        Input_machine, Input_prod_machine, Input_semi_price, Input_total_price
    )

    storage = ToolStorage()

    # Zbieramy dane od użytkownika
    tool_data_input = data_to_AddCuttingTool(
        nr_edv=Input_EDVNumber().nr_edv,
        type_tool=Input_type_tool(),
        origin=Input_origin(),
        nr_edv_semi_finished_product=Input_semi_edv_number().nr_edv_semi_finished_product,
        kind_tool=Input_kind_tool(),
        production_detail=Input_prod_detail(),
        machine=Input_machine(),
        production_machine=Input_prod_machine(),
        semi_finished_product_price=Input_semi_price(),
        total_price=Input_total_price()
    )

    # Konwertujemy do CuttingTool
    new_tool = CuttingTool(
        nr_edv=tool_data_input.nr_edv,
        type_tool=tool_data_input.type_tool,
        origin=tool_data_input.origin,
        nr_edv_semi_finished_product=tool_data_input.nr_edv_semi_finished_product,
        kind_tool=tool_data_input.kind_tool,
        production_detail=tool_data_input.production_detail,
        machine=tool_data_input.machine,
        production_machine=tool_data_input.production_machine,
        semi_finished_product_price=tool_data_input.semi_finished_product_price,
        total_price=tool_data_input.total_price
    )

    # Dodajemy do magazynu
    adder = AddCuttingTool(storage)
    adder.add_tool(new_tool)

    print("\nAktualny magazyn narzędzi:")
    for tool in storage.storage:
        print(tool)
