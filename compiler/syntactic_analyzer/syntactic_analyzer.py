from constants import *
from .ll1_table import LL1_PARSING_TABLE


class SyntaticAnalyzer():
    #self._symbol_table = S

    def analyze(self, lexem, token):

        pilha = ["S", "$"]
        w = ''
        X = pilha[0]
        while X != "$":
            if  w != "$":
                if (token == IDENTIFIER_TOKEN) and (lexem not in RESERVED_WORDS):  
                    w = "ident" 
                else:
                    w = lexem 
            print(f'word: {w}', end = '  ')
            #print(f"Word: {w}", end= '  \n') # deletme


            try:
                if X == w:
                    pilha.pop(0)
                elif X in TERMINALS or LL1_PARSING_TABLE.get((X, w)) == None:
                    yield SyntacticProcessing.FAILED
                    
                else:
                    #print(f"({X}, {w}) -> {LL1_PARSING_TABLE[(X, w)][1]}")
                    pilha.pop(0)

                    for caracter in reversed((LL1_PARSING_TABLE[(X, w)][1].split(' '))):     # change name of variable caracter
                        #print(caracter)
                        if caracter == 'epslon': 
                            continue
                        pilha.insert(0, caracter)
            except KeyError:
                yield SyntacticProcessing.FAILED
            
            X = pilha[0]

            lexem, token = yield SyntacticProcessing.IN_PROGRESS   # Still executing
            # If it is the last iteration
            if (token == None):       
                w = "$"

        yield SyntacticProcessing.SUCCESS
