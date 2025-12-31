from data_models import CuttingTool
from edv_number import EDVNumber

class EDVNumberAlreadyInUseError(Exception):
    pass

class ToolStorage:
    def __init__(self):
        self._tools_by_edv: dict[str, CuttingTool] = {}

    def add(self, tool: CuttingTool):
        if tool.nr_edv in self._tools_by_edv:
            raise EDVNumberAlreadyInUseError(f"EDV {tool.nr_edv} is already used")
        self._tools_by_edv[tool.nr_edv] = tool

    def exists_by_edv(self, edv: EDVNumber) -> bool:
            return edv in self._tools_by_edv
    
    def get(self, edv: EDVNumber) -> CuttingTool | None:
        return self._tools_by_edv.get(edv)

    def all(self):
        return list(self._tools_by_edv.values())
        
if __name__ == "__main__":
    storage = ToolStorage()

    lista_narzedzi = storage.all()
    print(lista_narzedzi)
