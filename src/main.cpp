#include <fstream>
#include <vector>
#include <memory>
#include <iostream>

#include "constants.h"
#include "ident_diagram.h"
#include "int_const_diagram.h"
#include "float_const_diagram.h"
#include "string_const_diagram.h"

using namespace std;

int main() {
    // Vector to hold the different diagram parsers.
    vector<unique_ptr<Diagram>> diagrams;
    diagrams.push_back(make_unique<IdentDiagram>());
    diagrams.push_back(make_unique<IntConstDiagram>());
    diagrams.push_back(make_unique<FloatConstDiagram>());

    // Input and output file streams.
    ifstream inputFile(INPUT_FILE);
    ofstream outputFile(OUTPUT_FILE);

    // Check if the input/output files are open.
    if (!inputFile.is_open() || !outputFile.is_open()) {
        cerr << "Error opening files!" << endl;
        return 1;
    }

    // Initialize variables for processing the input file.
    int line_number = 0;
    int column_number = 0;
    char c;
    bool is_processing = false;
    char character_to_backtrack = '\0';
    size_t completed_process_diagrams = 0;
    size_t number_diagrams = diagrams.size();
    string current_lexem = "";
    string current_token = "";
    pair<DiagramProcessing, pair<string, string>> result;
    int still_reading_file = 2; // Control flag for handling EOF processing.

    // Main processing loop.
    while (still_reading_file) { 

        // Handle EOF scenario.
        if (inputFile.peek() == EOF) {    
            still_reading_file--;
            c = ' ';
        } else {
            inputFile.get(c); 
            column_number++;
            if (c == '\n') {
                line_number++;
                column_number = 0;
            }
        }

        // Skip whitespace characters if not processing.
        if (!is_processing && isspace(c)) {
            continue;
        }

        // Check if all diagrams have finished processing.
        if (completed_process_diagrams == number_diagrams) {
            is_processing = false;
            completed_process_diagrams = 0;

            // Output the token and lexeme.
            outputFile << current_token << " ";
            current_lexem.clear();
            current_token.clear();

            // Reset all diagrams for the next round of processing.
            for (auto& diagram : diagrams) {
                diagram->reset();
            }

            // Exit the loop if EOF is reached and processing has finished.
            if (still_reading_file != 2) {
                still_reading_file = 0;
                continue;
            }

            // Handle backtracking of the character.
            if (character_to_backtrack == '\0') {
                inputFile.seekg(-1, ios::cur); // Go back one character.
                continue;
            } else {
                inputFile.seekg(-1, ios::cur);
                c = character_to_backtrack;
                character_to_backtrack = '\0'; // Clear backtrack after using it.
            }
        }

        // Start processing the character.
        completed_process_diagrams = 0;
        is_processing = true;

        // Loop through each diagram and process the character.
        for (auto& diagram : diagrams) {
            result = diagram->parse(c);

            switch (result.first) {
                case IN_PROGRESS:
                    // Still processing, continue.
                    break;

                case FINISHED:
                    // Check if the lexeme is longer than the current one, update token and lexeme.
                    if (result.second.second.length() > current_lexem.length()) {
                        current_token = result.second.first;
                        current_lexem = result.second.second;
                        character_to_backtrack = '\0'; // No need to backtrack.
                    }
                    completed_process_diagrams++;
                    break;

                case FINISHED_AND_BACKTRACK:
                    // Update token and lexeme, set backtrack character if necessary.
                    if (result.second.second.length() > current_lexem.length()) {
                        current_token = result.second.first;
                        current_lexem = result.second.second;
                        character_to_backtrack = isspace(c) ? '\0' : c;
                    }
                    completed_process_diagrams++;
                    break;

                case FAILED:
                    // Mark diagram as failed and increment completed count.
                    if (current_token.empty()) {
                        current_token = result.second.first;
                    }
                    completed_process_diagrams++;
                    break;

                default:
                    assert(false); // This state should not occur.
                    break;
            }
        }
    }

    // Close the input and output files.
    inputFile.close();
    outputFile.close();

    return 0;
}
