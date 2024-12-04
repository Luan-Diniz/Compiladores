from .diagram import *

class SepDiagram(Diagram):
    """
        Identifies the caracteres that are separators '(',')','[', ']', ',' , ';'
        Note: '{' and '}' have their own diagram. 
    """

    separators = ["(", ")", "[", "]", ",", ";"]
    def __init__(self) -> None:
        super().__init__()

    def parse(self, entry: str) -> tuple[int, tuple[str, str]]:
        # Processing has ended.
        if self._processing_state != DiagramProcessing.IN_PROGRESS:
            return self._result

        # Inicialização de pares de token e lexema
        token_and_lexem: tuple[str, str] = ("", "")
        return_pair: tuple[int, tuple[str, str]] = (DiagramProcessing.IN_PROGRESS, ("", ""))

        if self._current_state == 0:
            if entry in SepDiagram.separators:
                self._current_lexem += entry
                token_and_lexem = (SEP_TOKEN, self._current_lexem)
                return_pair = (DiagramProcessing.FINISHED, token_and_lexem)
            else:
                token_and_lexem = (GENERIC_TOKEN, "")
                return_pair =  (DiagramProcessing.FAILED, token_and_lexem)


        else:
            assert False  # Shouldn't run this.

        # Atualizando estado de processamento
        self._processing_state = return_pair[0]
        if self._processing_state != DiagramProcessing.IN_PROGRESS:
            self._result = return_pair

        return return_pair