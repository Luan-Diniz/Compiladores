#include "diagram.h"

void Diagram::reset() {
    _processing_state = IN_PROGRESS;
    _current_state = 0;
    _current_lexem = "";
    _result = {};
}