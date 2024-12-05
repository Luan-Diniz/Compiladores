from lexical_analyzer.lexical_analyzer import LexicalAnalyzer
from syntactic_analyzer.syntactic_analyzer import SyntaticAnalyzer
from symbol_table import SymbolTable

la = LexicalAnalyzer()
sa = SyntaticAnalyzer()

for lexem, token in la.analyze():
    
    result = sa.analyze(lexem, token)
    
    print(result)
    # ToDo: Integrar com o analisador sintatico

#print(SymbolTable().get_all_occurrences()) # Teste Singleton