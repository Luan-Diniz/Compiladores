from constants import *
from .ll1_table import LL1_PARSING_TABLE


class SyntaticAnalyzer():
    #self._symbol_table = S

    def analyze(self, lexem, token):

        if token == IDENTIFIER_TOKEN and lexem not in RESERVED_WORDS:
            w = "ident" + "$"
        else:
            w = lexem + "$"

        print(w, end='   Result:')

        i = 0
        pilha = ["S", "$"]

        X = pilha[0]
        while X != "$":
            try:
                if X == w[i]:
                    pilha.pop(0)
                    i += 1
                elif X in TERMINALS or LL1_PARSING_TABLE.get((X, w[i])) == None:
                    return False
                    
                else:
                    #print(f"({X}, {w[i]}) -> {LL1_PARSING_TABLE[(X, w[i])][1]}")
                    pilha.pop(0)

                    for caracter in reversed(list(LL1_PARSING_TABLE[(X, w[i])][1])):     # LOGICA ERRADA --> Usar split(' ')??
                    if caracter == 'epslon' or '': 
                        continue
                    pilha.insert(0, caracter)
            except KeyError:
                return False
            
            X = pilha[0]

        return True
