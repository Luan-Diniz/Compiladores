#include "ident_diagram.h"

/*
    See diagram.h 
*/
std::pair<DiagramProcessing,
 std::pair<std::string, std::string>> IdentDiagram::parse(const char entry) {

    std::pair<std::string, std::string> token_and_lexem;
    std::pair<DiagramProcessing, std::pair<std::string, std::string>> return_pair;

    switch (_current_state)
    {
        case 0:
            token_and_lexem.second = "";

            if (isalpha(entry)) {
                _current_state = 1;
                _current_lexem += entry;

                return_pair.first = IN_PROGRESS;
                return_pair.second = token_and_lexem;
            } else {
                token_and_lexem.first = GENERIC_TOKEN;
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

            } else {
                // _current_state = 2;
                token_and_lexem.first = IDENTIFIER_TOKEN;
                token_and_lexem.second = _current_lexem;
                return_pair.first = FINISHED_AND_BACKTRACK;
                return_pair.second = token_and_lexem;
            }
            break;
            
        default:
            assert(false);  // Should not get here.
            break;
    }

    // Gets ready to process a new token.
    if (return_pair.first != IN_PROGRESS) {
        reset();
    }

    return return_pair;
}

