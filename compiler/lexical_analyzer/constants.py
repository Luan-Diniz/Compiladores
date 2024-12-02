from enum import Enum, auto

# Reserved words      # TODO: Verificar as palavras reservadas que faltam
RESERVED_WORDS = (
    "def", "if", "else", "print", "read", "return", "int", "float",
    "string", "for", "new", "null", "break"  
)

RESERVED_WORDS_SIZE = len(RESERVED_WORDS)

# File paths
INPUT_FILE = "input_files/source_code_example.txt"
OUTPUT_FILE = "output_files/parse.txt"
SYMBOL_TABLE_FILE = "output_files/symbol_table.txt"

# Token types
GENERIC_TOKEN = "OUTRO"
IDENTIFIER_TOKEN = "IDENT"
INTEGER_TOKEN = "NI"
FLOAT_TOKEN = "NPF"
STRING_TOKEN = "A DEFINIR STRINGTOKEN"         # TODO: Definir o resto dos tokens

# Enum for diagram processing states
class DiagramProcessing(Enum):
    IN_PROGRESS = auto(),
    FINISHED = auto(),
    FINISHED_AND_BACKTRACK = auto(),
    FAILED = auto(),