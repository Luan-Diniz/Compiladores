from  constants import *

'''

# ToDo

import os

def get_userdef_terminals() -> list:
    try:
        # Coleta os caracteres da tabela de símbolos até encontrar um ":"
        with open(SYMBOL_TABLE_FILE, 'r') as symbol_table:
            terminals = [line.split(':')[0].strip() for line in symbol_table]
            return terminals
    except:
        print("Error opening files!")
        return []


class SyntacticAnalyzer:
    def __init__(self):
        pass

    def analyze(self) -> bool:
        # Abre os arquivos de entrada e saída
        if not os.path.isfile(INPUT_FILE):
            print("Input file does not exist!")
            return False
        try:
            inputFile = open(INPUT_FILE, 'r')
            outputFile = open(OUTPUT_FILE, 'w')
        except IOError:
            print("Error opening files!")
            return False

        # w = input_file
        w = w.replace("0M", "a").replace("1M", "b").replace("0m", "c").replace("1m", "d")
        w += "$"
        
        print(w)

        i = 0
        pilha = ["S", "$"]

        X = pilha[0]
        while X != "$":

            if X == w[i]:
                pilha.pop(0)
                i += 1
            elif X in TERMINALS or LL1_PARSING_TABLE[(X, w[i])] == '':
                return False
                
            else:
                print(f"({X}, {w[i]}) -> {LL1_PARSING_TABLE[(X, w[i])][1]}"
                    .replace("a", "0M").replace("b", "1M").replace("c", "0m")
                    .replace("d", "1m").replace("C", "B'"))
                pilha.pop(0)

                for caracter in reversed(list(LL1_PARSING_TABLE[(X, w[i])][1])):
                    pilha.insert(0, caracter)
            
            X = pilha[0]

        # Fecha arquivos e escreve a tabela de símbolos
        inputFile.close()
        outputFile.close()

        return True
'''