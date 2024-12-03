# TODO: Esta tabela de símbolos é muito simples e incompleta.
class SymbolTable():
    def __init__(self) -> None:
        self.__table: dict[str, dict[str,]] = {}

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