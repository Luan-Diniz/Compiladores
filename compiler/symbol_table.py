# TODO: Esta tabela de símbolos é muito simples e incompleta.
class SymbolTable():
    _instance = None

    # Singleton
    def __new__(cls):           
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


    def __init__(self) -> None:
        if not hasattr(self, "_initialized"):
            self.__table: dict[str, dict[str,]] = {}
            self._initialized = True

    def add(self, symbol: str, line: int, column: int):
        entry = self.__table.get(symbol, None)
        if entry:
            self.__table[symbol]["occurrences"].append((line,column))
        else:
            self.__table[symbol] = {
                "occurrences": [(line, column)]
            }
            
    def get(self, symbol: str):
        return self.__table.get(symbol, None)

    def get_all_occurrences(self):
        return self.__table
    
    