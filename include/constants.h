#ifndef CONSTANTS_H
#define CONSTANTS_H

#include <iostream>
#include <unordered_map>
#include <unordered_set>
#include <vector>
#include <string>
#include <utility>

using namespace std;

typedef pair<int, int> LineColumnPair;
typedef vector<LineColumnPair> OccurrenceVector;
typedef unordered_map<string, OccurrenceVector> Table;

// Reserved words
const unordered_set<std::string> reserved_words_set = {
    "def", "if", "else", "print", "read", "return",
    "int", "float", "string", "for", "new", "null", "break", 
    "and", "not", "or", "tint", "tfloat", "tstring"};
const int reserved_words_size = 16;

// File paths
const string INPUT_FILE = "input_files/source_code_example.txt";
const string OUTPUT_FILE = "output_files/parse.txt";
const string SYMBOL_TABLE_FILE = "output_files/symbol_table.txt";

// Token types
const string GENERIC_TOKEN = "OUTRO";
const string IDENTIFIER_TOKEN = "IDENT";
const string INTEGER_TOKEN = "NI";
const string FLOAT_TOKEN = "NPF";
const string STRING_TOKEN = "A DEFINIR STRINGTOKEN";

// Enum for diagram processing states
enum DiagramProcessing
{
    IN_PROGRESS,
    FINISHED,
    FINISHED_AND_BACKTRACK,
    FAILED
};

#endif // CONSTANTS_H
