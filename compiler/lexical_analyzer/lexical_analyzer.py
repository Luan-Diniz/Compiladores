'''
class LexicalAnalyzer():
    def __init__(self):
        pass
'''

from lexical_analyzer.ident_diagram import IdentDiagram
from lexical_analyzer.int_const_diagram import IntConstDiagram
from lexical_analyzer.float_const_diagram import FloatConstDiagram
from lexical_analyzer.string_const_diagram import StringConstDiagram
from lexical_analyzer.diagram import *
from symbol_table import SymbolTable
import os


class LexicalAnalyzer:
    def __init__(self):
        self.diagrams: list[Diagram ] = [
            IdentDiagram(),
            IntConstDiagram(),
            FloatConstDiagram(),
            StringConstDiagram(),
        ]
        self.symbol_table = SymbolTable()
        self.number_diagrams = len(self.diagrams)


    def is_reserved_word(self, lexem: str) -> bool:
        return lexem in RESERVED_WORDS


    def write_to_table(self):
        # Escreve na tabela de símbolos
        try:
            with open(SYMBOL_TABLE_FILE, 'w') as symbol_table_file:
                entries = self.symbol_table.get_all_occurrences()
                for entry, properties in entries.items():
                    occurrences = properties["occurrences"]
                    if self.is_reserved_word(entry):
                        continue
                    symbol_table_file.write(f"{entry}: "+"{")
                    symbol_table_file.write(" ".join(
                        f"({line},{col})" for line, col in occurrences))
                    symbol_table_file.write("}\n")
        except IOError:
            print("Error opening symbol table file!")

    def analyze(self):
        # Abre os arquivos de entrada e saída
        if not os.path.isfile(INPUT_FILE):
            print("Input file does not exist!")
            return
        try:
            inputFile = open(INPUT_FILE, 'r')
            outputFile = open(OUTPUT_FILE, 'w')
        except IOError:
            print("Error opening files!")
            return

        # Inicializa variáveis de controle
        line_number = 1
        column_number = 0
        to_write_line = 0
        to_write_column = 0
        is_processing = False
        character_to_backtrack = ''
        completed_process_diagrams = 0
        current_lexem = ""
        current_token = ""
        still_reading_file = 2  # Controle para EOF

        # Loop principal
        while still_reading_file:
            # Lida com o EOF
            c = inputFile.read(1)
            if not c:  # Se EOF
                still_reading_file -= 1
                c = ' '
            column_number += 1
            if c == '\n':
                line_number += 1
                column_number = 0

            # Ignora espaços em branco
            if not is_processing and c.isspace():
                continue

            # Checa se todos os diagramas finalizaram o processamento
            if completed_process_diagrams == self.number_diagrams:
                is_processing = False
                completed_process_diagrams = 0

                # Escreve o token e lexema no arquivo de saída
                outputFile.write(f"{current_token} ")
                if current_token == IDENTIFIER_TOKEN:
                    self.symbol_table.add(current_lexem, to_write_line,
                                          to_write_column - len(current_lexem))
                current_lexem = ""
                current_token = ""

                # Reseta os diagramas
                map(lambda x: x.reset(), self.diagrams)
                # for diagram in self.diagrams:
                #     diagram.reset()

                # Checa se EOF foi alcançado
                if still_reading_file != 2:
                    still_reading_file = 0
                    continue

                # Trata o retrocesso do caractere
                if character_to_backtrack == '\0':
                    inputFile.seek(inputFile.tell() - 1)
                    c = character_to_backtrack
                    character_to_backtrack = ''
                    continue

            # Inicia o processamento
            completed_process_diagrams = 0
            is_processing = True

            # Processa o caractere com cada diagrama
            for diagram in self.diagrams:
                result = diagram.parse(c)

                if result[0] == DiagramProcessing.IN_PROGRESS:
                    continue

                elif result[0] == DiagramProcessing.FINISHED:
                    if len(result[1][1]) > len(current_lexem):
                        to_write_column = column_number
                        to_write_line = line_number
                        current_token = result[1][0]
                        current_lexem = result[1][1]
                        character_to_backtrack = ''

                    completed_process_diagrams += 1

                elif result[0] == DiagramProcessing.FINISHED_AND_BACKTRACK:
                    if len(result[1][1]) > len(current_lexem):
                        to_write_column = column_number
                        to_write_line = line_number
                        current_token = result[1][0]
                        current_lexem = result[1][1]
                        character_to_backtrack = c if not c.isspace() else ''

                    completed_process_diagrams += 1

                elif result[0] == DiagramProcessing.FAILED:
                    completed_process_diagrams += 1

        # Fecha arquivos e escreve a tabela de símbolos
        inputFile.close()
        outputFile.close()
        self.write_to_table()