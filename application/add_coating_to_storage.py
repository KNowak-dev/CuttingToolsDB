from coating_storage import CoatingStorage
from data_models import CoatingTool
from coating_storage import CoatingNameAlreadyInUseError

class AddCoatingToStorage:
    def __init__(self, coating: CoatingStorage):
        self.tool_coating = coating
    
    def add_coating(self, data: CoatingTool) -> CoatingTool:
        if self.tool_coating.exists_by_coating_name(data.coating_name):
            raise CoatingNameAlreadyInUseError(f"EDV number {data.coating_name} is already exist.")

        coating = CoatingTool(
                coating_name=data.coating_name,
                coating_width=data.coating_width,
                coating_factory=data.coating_factory,
                coating_in_progress=data.coating_in_progress)

        self.tool_coating.add_coating_name(coating)
        return coating
    
if __name__ == "__main__":
    from input_coating_info import (Input_Coating_name, Input_Coating_Width, Input_Coating_Factory, Input_coating_in_progress)

    coating_storage= CoatingStorage()

    adder = AddCoatingToStorage(coating_storage)
    
    coating_name = Input_Coating_name()
    coating_width = Input_Coating_Width()
    coating_factory = Input_Coating_Factory()
    coating_in_progress = Input_coating_in_progress()

    coating_data = CoatingTool(
        coating_name=coating_name,
        coating_width=coating_width,
        coating_factory=coating_factory,
        coating_in_progress=coating_in_progress)

    try:
        new_coating = adder.add_coating(coating_data)
        print(f"Nazwa powłoki: {new_coating.coating_name}, Grubość: {new_coating.coating_width}, Firma: {new_coating.coating_factory}, Iloś w powlekaniu: {new_coating.coating_in_progress}")
    except CoatingNameAlreadyInUseError as e:
        print(e)

    print("Lista powłok w magazynie:", coating_storage.all())
