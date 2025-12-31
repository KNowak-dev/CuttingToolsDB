from edv_number import EDVNumber
from semi_edv_number import EDVNumberSemiProduct
from tools_storage import ToolStorage
from data_models import data_to_AddCuttingTool
from add_tool import AddCuttingTool

def Input_EDVNumber():
    edv = EDVNumber.validate_edv(str(input("Wprowadź nr edv: ")))

    return edv        
           
def Input_type_tool():
    type_tool_to_choose = ["Toczne", "Obrotowe"]

    print("Wybierz typ: ")
    for item in type_tool_to_choose:
        print("- ", item)

    type_tool = input("Twój wybór: ")

    if not (type_tool == "Obrotowe" or type_tool == "Toczne"):
        raise ValueError("Nieprawidłowy wybór.")
        
    return type_tool
        
def Input_origin():
    origin_to_choose = ["Kupne", "Produkowane"]

    print("Wybierz pochodzenie: ")
    for item in origin_to_choose:
        print("- ", item)

    origin = input("Twój wybór: ")

    if not (origin == "Kupne" or origin == "Produkowane"):
        raise ValueError("Nieprawidłowy wybór!")
        
    return origin     


def Input_semi_edv_number():
    edv_semi_product = EDVNumberSemiProduct.validate_edv_semi(str(input("Wprowadź nr edv półfabrykatu: ")))

    return edv_semi_product

def Input_kind_tool():
    kind_tool_to_choose = {1 : "Wiertło", 
                       2 : "Nawiertak", 
                       3 : "Rozwiertak", 
                       4 : "Pogłębiacz", 
                       5 : "Gratownik", 
                       6 : "Płytka", 
                       7 : "Nóż tokarski"}
    
    print("Wybierz rodzaj narzędzia: ")
    for item in kind_tool_to_choose.items():
        print("- ", item)
    
    choice = int(input("Twój wybór: "))
        
    kind_tool = kind_tool_to_choose.get(choice)
    if not kind_tool:
        return None

    return kind_tool
        
def Input_prod_detail():
    production_detail_to_choose = { 1 : "Antriebswelle", 
                                2 : "Gewindestueck", 
                                3 : "Huelse", 
                                4 : "Polkern", 
                                5 : "Bodenstueck", 
                                6 : "Conical", 
                                7 : "Kolben",
                                8 : "Kolbenfuehrung",
                                9 : "Magnetkern",
                                10 : "Magnethuelse",
                                11 : "Welle",
                                12 : "Zentralventilgehause",
                                13 : "Gehause"}
    
    print("Wybierz detal produkcyjny: ")
    for item in production_detail_to_choose.items():
        print("- ", item)

    prod_detail = int(input("Twój wybór: "))

    production_detail = production_detail_to_choose.get(prod_detail)
        
    if not production_detail:
        return None

    return production_detail

def Input_machine():
    machine_to_choose = { 1 : "TTB", 
                    2 : "ANCA", 
                    3 : "Rollomatic", 
                    4 : "HAAS", 
                    5 : "Walter", 
                    6 : "EWAG", 
                    7 : "COM",
                    8 : "Brak"
                    }
    
    print("Wybierz maszynę do produkowania narzędzia: ")
    for item in machine_to_choose.items():
        print("- ", item)

    mach = int(input("Twój wybór: "))
    machine = machine_to_choose.get(mach)

    if not machine:
        return None
        
    return machine

def Input_prod_machine():
    production_maschine_to_choose = { 1 : "GM-20", 
                        2 : "Index-32", 
                        3 : "Index-36", 
                        4 : "Index-40", 
                        5 : "SG-18", 
                        6 : "SC7-36", 
                        7 : "SC9-40",
                        8 : "Benzinger",
                        9 : "DMG Multisprint 36",
                        10 : "Tornos",
                        11 : "Traub TNK36",
                        12 : "Traub TNX32",
                        13 : "GS-18"}
    
    print("Wybierz maszynę produkcyjną, na której pracuje narzędzie: ")
    for item in production_maschine_to_choose.items():
        print("- ", item)

    prod_machine = int(input("Twój wybór: "))

    production_machine = production_maschine_to_choose.get(prod_machine)
    
    if not production_machine:
        return None

    return production_machine

def Input_semi_price():
    print("Cena półfabrykatu:\n")
    try:
        semi_finished_product_price = float(input("Wprowadź cenę półfabrykatu."))
    except ValueError:
        print("Nieprawidłowy format danej.")
        return None

    return semi_finished_product_price

def Input_total_price(): 
    print("Wrpowadź całkowitą cene narzędzia: ")
    try:
        total_price = float(input("Wprowadź cenę narzędzia: "))
    except ValueError:
        print("Nieprawidłowy format danej.")
        return None
        
    return total_price

if __name__ == "__main__":
    storage = ToolStorage()

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
        total_price=total_price
)