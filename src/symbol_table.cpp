#include "symbol_table.h"

SymbolTable::SymbolTable()
{
}

void SymbolTable::add(string symbol, int line, int column)
{
    if (symbol_table.find(symbol) == symbol_table.end())
    {
        OccurrenceVector v;
        symbol_table.insert({symbol, v});
    }
    symbol_table[symbol].push_back(LineColumnPair(line, column));
}

OccurrenceVector SymbolTable::get(string symbol)
{
    return symbol_table[symbol];
}

vector<pair<string, OccurrenceVector>> SymbolTable::getAllOccurrences()
{
    vector<pair<string, OccurrenceVector>> all_occurrences;

    for (auto &entry : symbol_table)
    {
        all_occurrences.push_back(entry);
    }
    return all_occurrences;
}
