from lexical_analyzer.lexical_analyzer import LexicalAnalyzer
from symbol_table import SymbolTable

la = LexicalAnalyzer()

for output in la.analyze():
    print(output)
    
    # ToDo: Integrar com o analisador sintatico

#print(SymbolTable().get_all_occurrences()) # Teste Singleton