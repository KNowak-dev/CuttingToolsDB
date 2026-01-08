from dataclasses import dataclass
from typing import Optional
from edv_number import EDVNumber
from semi_edv_number import EDVNumberSemiProduct
from choose_type import InputTypeTool
from choose_origin import InputToolOrigin

@dataclass
class CoatingTool:
      coating_name: str = ""
      coating_width: int = 0
      coating_factory: str = ""
      coating_in_progress: int = 0
      coating_price: float = 0.0

@dataclass
class CuttingTool:
        nr_edv: Optional[EDVNumber] = None
        type_tool: Optional[str] = None
        origin: Optional[str] = None
        nr_edv_semi_finished_product: Optional[EDVNumberSemiProduct] = None
        kind_tool: str = ""
        production_detail: str = ""
        machine: str = ""
        production_machine: str = ""
        semi_finished_product_price: float = 0.0
        total_price: float = 0.0
        quantity: int = 0
        month_tools_consumption: int = 0
        coating: Optional[CoatingTool] = None
        
@dataclass
class data_to_AddCuttingTool:
    type_tool: Optional[str] = None
    origin: Optional[str] = None
    kind_tool: str
    production_detail: str
    machine: str
    production_machine: str
    semi_finished_product_price: float
    total_price: float
    quantity: int
    month_tools_consumption: int
    nr_edv: Optional[EDVNumber] = None
    nr_edv_semi_finished_product: Optional[EDVNumberSemiProduct] = None
