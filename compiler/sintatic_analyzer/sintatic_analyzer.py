from  lexical_analyzer.constants import SYMBOL_TABLE_FILE

def get_userdef_terminals():
    with open(SYMBOL_TABLE_FILE, 'r') as symbol_table:
        terminals = [line[0] for line in symbol_table]
        return terminals

