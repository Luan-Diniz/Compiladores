#include "symbol_table.h"

SymbolTable::SymbolTable() {

}

void SymbolTable::add(string symbol, int line, int column) {
    if (symbol_table.find(symbol) == symbol_table.end()) {
        OccuranceVector v;
        symbol_table.insert({symbol, v});
    }
    symbol_table[symbol].push_back(LineColumnPair(line, column));
}

OccuranceVector SymbolTable::get(string symbol) {
    return symbol_table[symbol];
}
