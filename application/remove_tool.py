from tools_storage import ToolStorage
from edv_number import EDVNumber

class RemoveTool:
    def __init__(self, tool_storage: ToolStorage):
        self.tool_storage = tool_storage
    
    def Remove_tool(self, edv: EDVNumber):
        if not self.tool_storage.exists_by_edv(edv):
            raise KeyError("EDV is not found.")
        
        del self.tool_storage._tools_by_edv[edv]

        print("Narzędzie o nr edv:", edv, "zostało usunięte.")

if __name__ == "__main__":
    pass
