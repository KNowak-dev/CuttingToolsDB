from tools_storage import ToolStorage
from coating_storage import CoatingStorage
from edv_number import EDVNumber

class AddCoatingToTool:
    def __init__(self, tool_storage: ToolStorage, coating_storage: CoatingStorage):
        self.tool_storage = tool_storage
        self.coating_storage = coating_storage

    def add(self, edv: EDVNumber, coating_name: str):
        tool = self.tool_storage.get(edv)
        if tool is None:
            raise KeyError(f"Tool with EDV {edv} not found")

        coating = self.coating_storage.get(coating_name)
        if coating is None:
            raise KeyError(f"Coating {coating_name} not found")

        tool.coating = coating
        return tool
    