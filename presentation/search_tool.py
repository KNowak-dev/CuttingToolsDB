from tools_storage import ToolStorage
from input_search_edv import InputSearchEDV
from edv_number import EDVNumber

class SearchTool:
    def __init__(self, storage_db: ToolStorage):
        self.storage_db = storage_db

    def SearchToolInStorageDB(self, edv: EDVNumber):
        tool = self.storage_db.get(edv)

        if tool is None:
            raise KeyError("EDV is not exist.")
        
        return tool
    
    def PrintInfoTool(self, tool):
        print("Nr EDV narzędzia:", tool.nr_edv)
        print("Typ narzędzia:", tool.type_tool)
        print("Kupne/Produkowane", tool.origin)
        print("Nr EDV półfabrykatu:", tool.nr_edv_semi_finished_product)
        print("Rodzaj narzędzia:", tool.kind_tool)
        print("Detal produkcyjny:",tool.production_detail)
        print("Maszyna, na której produkujemy narzędzie:", tool.machine)
        print("Maszyna produkcyjna, na której pracuje narzędzie:", tool.production_machine)
        print("Cena półfabrykatu:", tool.semi_finished_product_price)
        print("Cena narzędzia:", tool.total_price)
        print("Ilość narzędzi:", tool.quantity)
        print("Zużycie miesięczne:", tool.coating_in_progress)

        if tool.coating:
                print("Powłoka:", tool.coating.coating_name)
        else:
            print("Powłoka: brak")
        
if __name__ == "__main__":
    from input_search_edv import InputSearchEDV

    storage = ToolStorage()

    edv = InputSearchEDV()
    search = SearchTool(storage)
    
    try:
        tool = search.SearchToolInStorageDB(edv)
        search.PrintInfoTool(tool)
    except KeyError as e:
        print(e)
