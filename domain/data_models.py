from dataclasses import dataclass
from typing import Optional
from edv_number import EDVNumber
from semi_edv_number import EDVNumberSemiProduct

@dataclass
class CoatingTool:
      coating_name: str = ""
      coating_width: int = 0
      coating_factory: str = ""

@dataclass
class CuttingTool:
        nr_edv: Optional[EDVNumber] = None
        type_tool: str =""
        origin: str = ""
        nr_edv_semi_finished_product: Optional[EDVNumberSemiProduct] = None
        kind_tool: str = ""
        production_detail: str = ""
        machine: str = ""
        production_machine: str = ""
        semi_finished_product_price: float = 0.0
        total_price: float = 0.0
        coating: Optional[CoatingTool] = None
        
@dataclass
class data_to_AddCuttingTool:
    type_tool: str
    origin: str
    kind_tool: str
    production_detail: str
    machine: str
    production_machine: str
    semi_finished_product_price: float
    total_price: float
    nr_edv: Optional[EDVNumber] = None
    nr_edv_semi_finished_product: Optional[EDVNumberSemiProduct] = None
