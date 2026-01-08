def Input_Coating_name():
    coating_name = str(input("Wprowadź nazwę powłoki:"))

    return coating_name

def Input_Coating_Width():
    while True:
        try:
            coating_width = int(input("Wprowadź grubość powłoki: "))
            if coating_width < 0:
                print("Ilość nie może być ujemna.")
                continue
            return coating_width
        except ValueError:
            print("Wprowadź poprawną liczbę całkowitą.")
    
def Input_Coating_Factory():
    coating_factory = str(input("Wprwoadź nazwę fimry powlekającej:"))

    return coating_factory

def Input_coating_in_progress():
    while True:
        try:
            coating_in_progress = int(input("Wprowadź ilość narzędzi wysłanych do powlekania: "))
            if coating_in_progress < 0:
                print("Ilość nie może być ujemna.")
                continue
            return coating_in_progress
        except ValueError:
            print("Wprowadź poprawną liczbę całkowitą.")

def Input_coating_price():
    while True:
        try:
            coating_price = float(input("Wprowadź cenę powlekania:"))
            if coating_price < 0:
                print("Ilość nie może być ujemna.")
                continue
            return coating_price
        except ValueError:
            print("Wprowadź poprawną liczbę całkowitą.")
