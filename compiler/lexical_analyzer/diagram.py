from abc import abstractclassmethod, ABC
from constants import DiagramProcessing

class Diagram(ABC):

    def __init__(self) -> None:
        self._processing_state: DiagramProcessing = DiagramProcessing.IN_PROGRESS
        self._result: tuple[DiagramProcessing, tuple[str, str]] = (DiagramProcessing.IN_PROGRESS, ("", ""))
        self._current_state: int = 0
        self._current_lexem: str = ""


    @abstractclassmethod
    def parse(self) -> tuple[DiagramProcessing, tuple[str, str]]:
        """
        DiagramProcessing:
            IN_PROGRESS: It is processing the token.
            FAILED: The Diagram has not accepted the entries.
            FINISHED: Has completed the token processment (it was accepted).
            FINISHED_AND_BACKTRACK: Has completed the token processment (it was accepted)
            and the pointer should backtrack one character.
        tuple[str, str]:
            First:
                When the processment has been completed, stores the token.
            Second:
                Stores the lexem. 
        """

        pass 

    def reset(self) -> None:
        self._processing_state = DiagramProcessing.IN_PROGRESS
        self._current_state = 0
        self._current_lexem = ""
        self._result = []