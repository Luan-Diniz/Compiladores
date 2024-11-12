from diagram import *


class FloatConstDiagram(Diagram):
    def __init__(self) -> None:
        super().__init__()

    # See diagram.py
    def parse(self, entry: str) -> tuple[int, tuple[str, str]]:
        # Processing has ended.
        if self._processing_state != DiagramProcessing.IN_PROGRESS:
            return self._result

        # Inicialização de pares de token e lexema
        token_and_lexem: tuple[str, str] = ("", "")
        return_pair: tuple[int, tuple[str, str]] = (DiagramProcessing.IN_PROGRESS, ("", ""))

        # Switch case simulada usando if-elif-else
        if self._current_state == 0:
            if entry.isdigit():
                self._current_state = 1
                self._current_lexem += entry

                token_and_lexem = ("", "")
                return_pair = (DiagramProcessing.IN_PROGRESS, token_and_lexem)
            else:
                token_and_lexem = (GENERIC_TOKEN, "")
                return_pair = (DiagramProcessing.FAILED, token_and_lexem)

        elif self._current_state == 1:
            if entry.isdigit():
                # self._current_state = 1
                self._current_lexem += entry

                token_and_lexem = ("", "")
                return_pair = (DiagramProcessing.IN_PROGRESS, token_and_lexem)

            elif entry == '.':
                self._current_state = 2
                self._current_lexem += entry

                token_and_lexem = ("", "")
                return_pair = (DiagramProcessing.IN_PROGRESS, token_and_lexem)

            else:
                token_and_lexem = (GENERIC_TOKEN, "")
                return_pair = (DiagramProcessing.FAILED, token_and_lexem)

        elif self._current_state == 2:
            if entry.isdigit():
                self._current_lexem += entry

                token_and_lexem = ("", "")
                return_pair = (DiagramProcessing.IN_PROGRESS, token_and_lexem)
            else:
                token_and_lexem = (FLOAT_TOKEN, self._current_lexem)
                return_pair = (DiagramProcessing.FINISHED_AND_BACKTRACK, token_and_lexem)

        else:
            assert False  # Shouldn't run this.

        # Atualizando estado de processamento
        self._processing_state = return_pair[0]
        if self._processing_state != DiagramProcessing.IN_PROGRESS:
            self._result = return_pair

        return return_pair
