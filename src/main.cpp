#include <fstream>
#include <vector>
#include <memory>

#include "constants.h"
#include "ident_diagram.h"
#include "int_const_diagram.h"
#include "float_const_diagram.h"
#include "string_const_diagram.h"

using namespace std;

int main()
{
    vector<unique_ptr<Diagram>> diagrams;
    diagrams.push_back(make_unique<IdentDiagram>());
    diagrams.push_back(make_unique<IntConstDiagram>());
    diagrams.push_back(make_unique<FloatConstDiagram>());

    ifstream inputFile(INPUT_FILE);
    ofstream outputFile(OUTPUT_FILE);

    if (!inputFile.is_open() || !outputFile.is_open()) {
        cerr << "Error opening files!" << endl;
        return 1;
    }

    // Process input file.
    char c;
    bool is_processing = false;
    char character_to_backtrack = '\0';
    size_t completed_process_diagrams;
    size_t number_diagrams = diagrams.size();
    string current_lexem = "";
    string current_token = "";
    pair<DiagramProcessing, pair<string, string>> result;
    int still_reading_file = 2;
    while (still_reading_file) { 

        // To finish the processing when it has not finished but the file ended.
        if (inputFile.peek() == EOF) {    
            still_reading_file--;
            c = ' ';
        } else {
            inputFile.get(c); 
        }

        if (!is_processing and isspace(c)) {
            continue;
        }

        if (completed_process_diagrams == number_diagrams) {
            is_processing = false;
            completed_process_diagrams = 0;
            // Here saves token and/or lexems.
            /* // JUST FOR DEBUG.
            cout << "Token: " << current_token << endl;
            cout << "Lexem: " << current_lexem << endl;
            cout << endl;
            */

            outputFile << current_token << " ";
            current_lexem = "";
            current_token = "";    

            // Reset diagrams
            for (auto& diagram : diagrams) {
                diagram->reset();
            }

            if (still_reading_file != 2) {  // To don't duplicate the output when processing has already finish.
                still_reading_file = 0;
                continue;
            }

            if (character_to_backtrack == '\0') {
                inputFile.seekg(-1, ios::cur);    // Maybe change the 'character_to_backtrack' logic and use seekg as well!
                continue;
            } else {
                inputFile.seekg(-1, ios::cur);
                c = character_to_backtrack;
                character_to_backtrack = '\0';    // And execution continues using the caracter in backtrack.
            }
        }

        completed_process_diagrams = 0;
        is_processing = true;

        //cout << "PROCESSANDO " << c << endl; // Just for debug.

        for (auto& diagram : diagrams) {
            result = diagram->parse(c);
           
            switch (result.first)
            {
                case IN_PROGRESS:
                    break;
                case FINISHED:
                    if (result.second.second.length() > current_lexem.length()) {
                        current_token = result.second.first;
                        current_lexem = result.second.second;
                        character_to_backtrack = '\0';
                    }
                    completed_process_diagrams++;
                    break;
                case FINISHED_AND_BACKTRACK:
                    if (result.second.second.length() > current_lexem.length()) {
                        current_token = result.second.first;
                        current_lexem = result.second.second;

                        if (isspace(c)) {
                            character_to_backtrack = '\0';
                        } else {
                            character_to_backtrack = c;
                        }
                    }
                    completed_process_diagrams++;
                    break;
                case FAILED:
                    if (current_token == "") {
                        current_token = result.second.first;
                    }
                    completed_process_diagrams++;
                    break;
                default:
                    assert(false);  // Shouldn't run this.
                    break;
            }
        }



    }

    inputFile.close();
    outputFile.close();

    return 0;
}