from constants import *
from .ll1_table import LL1_PARSING_TABLE
from symbol_table import SymbolTable

class SyntaticAnalyzer():
    #self._symbol_table = SymbolTable()  # A tabela de símbolos é um singleton.

    def analyze(self, lexem, token):

        # Poderia ser [S, "$"], porém teria que tirar a adição de "$" quando token = None
        pilha = ["PROGRAM", "$"]   
        w = ''
        X = pilha[0]

        concluded_interation = False
        while X != "$":
            if  w != "$":
                # null é uma constante, mas é igual ao seu lexema, logo n precisa ser tratado
                if (token == IDENTIFIER_TOKEN) and (lexem not in RESERVED_WORDS):  
                    w = "ident" 
                elif (token == INTEGER_TOKEN):
                    w = "int_constant"
                elif (token == FLOAT_TOKEN):
                    w = "float_constant"    
                elif (token == STRING_TOKEN):
                    w = "string_constant"
                else:
                    w = lexem 
            #print(f'word: {w}', end = '  ')

            try:
                if X == w:
                    pilha.pop(0)
                    concluded_interation = True
                elif X in TERMINALS or LL1_PARSING_TABLE.get((X, w)) == None:
                    print(w)
                    print(X)
                    yield SyntacticProcessing.FAILED
                    
                else:
                    #print(f"({X}, {w}) -> {LL1_PARSING_TABLE[(X, w)][1]}")
                    pilha.pop(0)

                    for caracter in reversed((LL1_PARSING_TABLE[(X, w)][1].split(' '))):     # change name of variable caracter
                        if caracter == 'epslon': 
                            continue
                        pilha.insert(0, caracter)
            except KeyError:
                yield SyntacticProcessing.FAILED
            
            X = pilha[0]

            if not concluded_interation:    # Continua até achar o terminal na pilha
                continue

            lexem, token = yield SyntacticProcessing.IN_PROGRESS   # Still executing
            concluded_interation = False
            # If it is the last iteration
            if (token == None):       
                w = "$"

        yield SyntacticProcessing.SUCCESS
