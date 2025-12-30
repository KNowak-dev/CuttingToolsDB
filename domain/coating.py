from dataclasses import dataclass
from add_tool import CuttingTool

@dataclass
class Coating(CuttingTool):
            
    coating_factory: str = ""
    coating_name: str = ""
    coating_price: float = 0.0

if __name__ == "__main__":
    coating_tool = Coating(
        nr_edv="",
        type_tool="",
        origin="",
        nr_edv_semi_finished_product="",
        kind_tool="",
        production_detail="",
        machine="",
        production_machine="",
        semi_finished_product_price=0.0,
        total_price=0.0,
        coating_factory="Firma",
        coating_name="Powłoka",
        coating_price=100.0
    )

    print(coating_tool)
    