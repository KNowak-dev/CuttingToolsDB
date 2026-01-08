from tools_storage import ToolStorage, EDVNumberAlreadyInUseError
from data_models import CuttingTool, data_to_AddCuttingTool

class AddCuttingTool:
    def __init__(self, storage: ToolStorage):
        self.tool_storage = storage

    def add_tool(self, data: data_to_AddCuttingTool) -> CuttingTool:
        if self.tool_storage.exists_by_edv(data.nr_edv):
            raise EDVNumberAlreadyInUseError(f"EDV number {data.nr_edv} is already in use.")

        tool = CuttingTool(nr_edv = data.nr_edv, 
                           type_tool=data.type_tool, 
                           origin=data.origin, 
                           nr_edv_semi_finished_product=data.nr_edv_semi_finished_product, 
                           kind_tool=data.kind_tool,
                           production_detail=data.production_detail, 
                           machine=data.machine, 
                           production_machine=data.production_machine,
                           semi_finished_product_price=data.semi_finished_product_price,
                           total_price=data.total_price,
                           quantity=data.quantity
                           )

        self.tool_storage.add(tool)
        return tool

if __name__ == "__main__":
    from user_input import (
        Input_EDVNumber, Input_type_tool, Input_origin,
        Input_semi_edv_number, Input_kind_tool,
        Input_prod_detail, Input_machine, Input_prod_machine,
        Input_semi_price, Input_total_price, Input_quantity, data_to_AddCuttingTool
    )

    storage = ToolStorage()

    # Pobieranie danych od użytkownika
    nr_edv = Input_EDVNumber()
    type_tool = Input_type_tool()
    origin = Input_origin()
    nr_edv_semi = Input_semi_edv_number()
    kind_tool = Input_kind_tool()
    prod_detail = Input_prod_detail()
    machine = Input_machine()
    prod_machine = Input_prod_machine()
    semi_price = Input_semi_price()
    total_price = Input_total_price()
    quantity = Input_quantity()

    # Tworzenie obiektu danych
    tool_data = data_to_AddCuttingTool(
        nr_edv=nr_edv,
        type_tool=type_tool,
        origin=origin,
        nr_edv_semi_finished_product=nr_edv_semi,
        kind_tool=kind_tool,
        production_detail=prod_detail,
        machine=machine,
        production_machine=prod_machine,
        semi_finished_product_price=semi_price,
        total_price=total_price,
        quantity=quantity
    )

    # Dodawanie narzędzia do magazynu
    adder = AddCuttingTool(storage)
    new_tool = adder.add_tool(tool_data)
    print(f"Dodano narzędzie: {new_tool}")
