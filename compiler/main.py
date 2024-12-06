from lexical_analyzer.lexical_analyzer import LexicalAnalyzer
from syntactic_analyzer.syntactic_analyzer import SyntaticAnalyzer
from symbol_table import SymbolTable
from syntactic_analyzer.ll1_table import LL1_PARSING_TABLE # for debug
from constants import *

la = LexicalAnalyzer()
sa = SyntaticAnalyzer()

lexical_iterator = la.analyze()
lexem, token = next(lexical_iterator)
syntactic_iterator = sa.analyze(lexem, token)

if next(syntactic_iterator) == SyntacticProcessing.FAILED:
        print('Erro sintático ocorreu')
        exit()

for lexem, token in lexical_iterator:
    print(f"Lexema: {lexem}, Token: {token}")
    result = syntactic_iterator.send((lexem, token)) 

    if result == SyntacticProcessing.FAILED:
        print('Erro sintático ocorreu')
        exit()
    if result == SyntacticProcessing.SUCCESS:
        print('Análise sintática feita com sucesso.')
        #break

#print(SymbolTable().get_all_occurrences()) # Teste Singleton