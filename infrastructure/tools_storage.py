from dataclasses import dataclass

# Magazyn/Baza wszystkich narzędzi, które zostały dodane - magazynem będzie lista, natomiast "obiekt" narzędzie jest dataclassą.

@dataclass
class ToolStorage:
    storage = []

    @classmethod
    def add_tool(cls, tool):
        cls.storage.append(tool)

if __name__ == "__main__":
    storage = ToolStorage()
    