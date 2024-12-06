from lexical_analyzer.lexical_analyzer import LexicalAnalyzer
from syntactic_analyzer.syntactic_analyzer import SyntaticAnalyzer
from constants import *

la = LexicalAnalyzer()
sa = SyntaticAnalyzer()

lexical_iterator = la.analyze()
lexem, token = next(lexical_iterator)
syntactic_iterator = sa.analyze(lexem, token)

# TODO: Lógica para mostrar linha e erro que erro sintático ocorreu.
if next(syntactic_iterator) == SyntacticProcessing.FAILED:
        print('Erro sintático ocorreu')
        exit()
sucess = False
try:
    for lexem, token in lexical_iterator:
        result = syntactic_iterator.send((lexem, token)) 

        if result == SyntacticProcessing.FAILED:
            print('Erro sintático ocorreu.')
            exit()
        if result == SyntacticProcessing.SUCCESS:
            sucess = True
except StopIteration:
    print('Erro sintático ocorreu.')
    sucess = False
if (sucess):
    print('Análise sintática concluída com sucesso.')