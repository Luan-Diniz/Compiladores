#ifndef SYMBOL_TABLE_H
#define SYMBOL_TABLE_H

#include "constants.h"

using namespace std;

class SymbolTable {

    public:
        SymbolTable();

        // Adds a new occurance.
        void add(string symbol, int line, int column);

        OccuranceVector get();

    private:   // Palavra reservada não estarão na tabela de símbolos.
        Table symbol_table;  
};


#endif