#include "string_const_diagram.h"

/*
    See diagram.h 
*/
std::pair<DiagramProcessing,
 std::pair<std::string, std::string>> StringConstDiagram::parse(const char entry) {

    // Processing has ended.
    if (_processing_state != IN_PROGRESS) {
        return _result;
    }

    std::pair<std::string, std::string> token_and_lexem;
    std::pair<DiagramProcessing, std::pair<std::string, std::string>> return_pair;

    switch (_current_state)
    {
        case 0:
            if (entry == '\"') {
                _current_state = 1;
                _current_lexem += entry;

                token_and_lexem = {"", ""};
                return_pair.first = IN_PROGRESS;
                return_pair.second = token_and_lexem;
            } else {
                token_and_lexem = {GENERIC_TOKEN, ""};
                return_pair.first = FAILED;
                return_pair.second = token_and_lexem;
            }
            break;
        
        case 1:
            if (isalnum(entry)) {
                // _current_state = 1;
                _current_lexem += entry; 

                token_and_lexem = {"", ""};
                return_pair.first = IN_PROGRESS;
                return_pair.second = token_and_lexem;

            } else if(entry == '\"') {
                // _current_state = 2; 
                token_and_lexem = {STRING_TOKEN, _current_lexem};
                return_pair.first = FINISHED;
                return_pair.second = token_and_lexem;
            } else {
                token_and_lexem = {GENERIC_TOKEN, ""};
                return_pair.first = FAILED;
                return_pair.second = token_and_lexem;
            }
            break;
            
        default:
            assert(false);  // Should'nt run this.
            break;
    }

    _processing_state = return_pair.first;
    if (_processing_state != IN_PROGRESS) {
        _result = return_pair;
    }

    return return_pair;
}