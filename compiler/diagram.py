from constants import *


class Diagram():
    def __init__(self) -> None:
        self._processing_state: DiagramProcessing = DiagramProcessing.IN_PROGRESS
        self._result: tuple[DiagramProcessing, tuple[str, str]] = (DiagramProcessing.IN_PROGRESS, ("", ""))
        self._current_state: int = 0
        self._current_lexem: str = ""
 
    # First:
    #     IN_PROGRESS: It is processing the token.
    #     FAILED: The Diagram has not accepted the entries.
    #     FINISHED: Has completed the token processment (it was accepted).
    #     FINISHED_AND_BACKTRACK: Has completed the token processment (it was accepted)
    #     and the pointer should backtrack one character.
    # Second:
    #     First:
    #         When the processment has been completed, stores the token.
    #     Second:
    #         Stores the lexem. 
    def  parse(self, entry: str) -> tuple[DiagramProcessing, tuple[str, str]]:
        pass
    
    #  Must be called before processing a new token.
    def reset(self):
        pass
  
