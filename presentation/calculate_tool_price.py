from tools_storage import ToolStorage
from edv_number import EDVNumber

class CalculateToolPrice:
    def __init__(self, tools_storage: ToolStorage):
        self.tools_storage = tools_storage

    def get_tool(self, edv: EDVNumber):
        tool = self.tools_storage.get(edv)

        if not tool:
            raise KeyError(f"EDV: {edv} is not found.")
        
        return tool
    
    def input_time_machine(self):
        try:
            tj = int(input("Wprowadź czas potrzebny na wyprodukowanie narzędzia w [min]:"))
        except ValueError:
            raise ValueError("Nieprawidłowa wartość. Wprowadź liczbę całkowitą.")

        if tj <= 0:
            raise ValueError("Czas musi być większy niż 0")
        
        return tj
        
    def input_cost_machine_working(self):
        try:
            h_cost = float(input("Wprowadź koszt [1h] pracy maszyny w PLN:"))
        except ValueError:
            raise ValueError("Nieprawidłowa wartość.")
        
        if h_cost <= 0:
            raise ValueError("Kwota musi być liczbą dodatnią.")
        
        return h_cost
    
    def calculate_tool_price(self, tool, tj, h_cost):
        if tool.origin.upper() == "KUPNE":
            tool_price = float(input("Wprowadź cenę katalogową narzędzia: "))
            return tool_price

        price_semi = tool.semi_finished_product_price
        coating_price = tool.coating.coating_price if tool.coating else 0

        total_price = price_semi + (tj * (h_cost / 60)) + coating_price
        return total_price
