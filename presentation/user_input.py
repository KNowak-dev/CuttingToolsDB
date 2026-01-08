from edv_number import EDVNumber
from semi_edv_number import EDVNumberSemiProduct
from tools_storage import ToolStorage
from data_models import data_to_AddCuttingTool
from add_tool import AddCuttingTool
from choose_type import InputTypeTool
from choose_origin import InputToolOrigin

def Input_EDVNumber():
    edv = EDVNumber.validate_edv(str(input("Wprowadź nr edv: ")))

    return edv        
           
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
    production_detail_to_choose = { 1 : "Tuleja", 
                                2 : "Wał", 
                                3 : "Wał korbowy", 
                                4 : "Panewka", 
                                5 : "Tarcza", 
                                6 : "Ślimacznica", 
                                7 : "Śruba pociągowa",
                                8 : "Trzpień",
                                9 : "Stożek morsa",
                                10 : "Koło zębate",
                                11 : "Koło zębate stożkowe",
                                12 : "Pierścień osadczy",
                                13 : "Dystans"}
    
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
    production_maschine_to_choose = { 1 : "Tokarka", 
                        2 : "Frezarka pionowa", 
                        3 : "Frezarka pozioma", 
                        4 : "Szlifierka kłowa", 
                        5 : "Frezarka obwiedniowa", 
                        6 : "Dłutownica", 
                        7 : "Szlifierka do płaszczyzn",
                        8 : "Tokarka karuzelowa",
                        9 : "Wiertarko-frezarka",
                        10 : "Tokarka CNC",
                        11 : "Frezarka CNC",
                        12 : "Wiertarka kolumnowa",
                        13 : "Wiertarka pionowa"}
    
    print("Wybierz maszynę produkcyjną, na której pracuje narzędzie: ")
    for item in production_maschine_to_choose.items():
        print("- ", item)

    prod_machine = int(input("Twój wybór: "))

    production_machine = production_maschine_to_choose.get(prod_machine)
    
    if not production_machine:
        return None

    return production_machine

def Input_semi_price():
    try:
        semi_finished_product_price = float(input("Wprowadź cenę półfabrykatu: "))
    except ValueError:
        print("Nieprawidłowy format danej.")
        return None

    return semi_finished_product_price

def Input_total_price(): 
    try:
        total_price = float(input("Wprowadź cenę narzędzia: "))
    except ValueError:
        print("Nieprawidłowy format danej.")
        return None
        
    return total_price

def Input_quantity():
    try:
        quantity = int(input("Wprowadź ilość sztuk."))
    except ValueError:
        print("Nieprawidłowy format danej.")
        quantity = 0
    
    return quantity

def Input_month_tools_consumption():
    try:
        consumption = int(input("Wprowadź zużycie miesięczne narzędzia:"))
    except ValueError:
        print(("Nieprawidłowy format danej."))
        consumption = 0

    return consumption

if __name__ == "__main__":
    storage = ToolStorage() 
    adder = AddCuttingTool(storage)
    type_tool = InputTypeTool(storage)
    origin = InputToolOrigin(storage)

    nr_edv = Input_EDVNumber()
    selected_type = type_tool.start_choose_type()
    origin_input = origin.start_choose_origin()
    nr_edv_semi = Input_semi_edv_number()
    kind_tool = Input_kind_tool()
    prod_detail = Input_prod_detail()
    machine = Input_machine()
    prod_machine = Input_prod_machine()
    semi_price = Input_semi_price()
    total_price = Input_total_price()
    quantity = Input_quantity()
    month_tools_consumption = Input_month_tools_consumption()

    if not selected_type or not origin_input:
        print("Nie wybrano typu lub pochodzenia narzędzia.")
        exit()

    tool_data = data_to_AddCuttingTool(
        nr_edv=nr_edv,
        type_tool=selected_type,
        origin=origin_input,
        nr_edv_semi_finished_product=nr_edv_semi,
        kind_tool=kind_tool,
        production_detail=prod_detail,
        machine=machine,
        production_machine=prod_machine,
        semi_finished_product_price=semi_price,
        total_price=total_price,
        quantity=quantity,
        month_tools_consumption=month_tools_consumption
)
    
    new_tool = adder.add_tool(tool_data)
    print(f"Dodano narzędzie: {new_tool}")
    print("Lista narzędzi w magazynie:", storage.all())