from data_models import CoatingTool
from coating import AddCoatingToStorage
from input_coating_info import Input_Coating_name, Input_Coating_Width, Input_Coating_Factory

class CoatingNameAlreadyInUseError(Exception):
    pass

class CoatingStorage:
    def __init__(self):
        self._coating_by_name: dict[str, CoatingTool] = {}

    def add_coating_name(self, coating: CoatingTool):
        if coating.coating_name in self._coating_by_name:
            raise CoatingNameAlreadyInUseError(f"EDV {coating.coating_name} is already exist")
        self._coating_by_name[coating.coating_name] = coating

    def exists_by_coating_name(self, coating_name: str) -> bool:
        return coating_name in self._coating_by_name
    
    def get(self, coating_name: str) -> CoatingTool | None:
        return self._coating_by_name.get(coating_name)
    
    def all(self):
        return list(self._coating_by_name.values())

if __name__ == "__main__":
    coating = CoatingStorage()

    adder = AddCoatingToStorage(coating)

    coating_name = Input_Coating_name()
    coating_width = Input_Coating_Width()
    coating_factory = Input_Coating_Factory()

    coating_data = CoatingTool(
        coating_name=coating_name,
        coating_width=coating_width,
        coating_factory=coating_factory)
    
    try:
        new_coating = adder.add_coating(coating_data)
        print(f"Nazwa powłoki: {new_coating.coating_name}, Grubość: {new_coating.coating_width}, Firma: {new_coating.coating_factory}")
    except CoatingNameAlreadyInUseError as e:
        print(e)
    
    print("Lista powłok w magazynie:", coating.all())
