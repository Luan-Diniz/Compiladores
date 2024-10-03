#ifndef CONSTANTS_H
#define CONSTANTS_H

#include <iostream>
#include <unordered_map>
#include <vector>
#include <string>
#include <utility>

using namespace std;

typedef pair<int, int> LineColumnPair;
typedef vector<LineColumnPair> OccurrenceVector;  
typedef unordered_map<string, OccurrenceVector> Table;

// Reserved words
const char *const reserved_words_array[] = {
    "def", "if", "else", "while", "print", "return", 
    "int", "float", "string", "bool", "true", 
    "false", "and", "or", "not", "in"
};
const int reserved_words_size = sizeof(reserved_words_array) / sizeof(reserved_words_array[0]);

// File paths
const string INPUT_FILE = "input_files/source_code_example.txt"; 
const string OUTPUT_FILE    = "output_files/parse.txt"; 

// Token types
const string GENERIC_TOKEN = "OUTRO";
const string IDENTIFIER_TOKEN = "IDENT";
const string INTEGER_TOKEN = "NI";
const string FLOAT_TOKEN = "NPF";
const string STRING_TOKEN = "A DEFINIR STRINGTOKEN"; 

// Enum for diagram processing states
enum DiagramProcessing {  
    IN_PROGRESS,  
    FINISHED,
    FINISHED_AND_BACKTRACK,
    FAILED
};

#endif // CONSTANTS_H
