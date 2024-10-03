#ifndef CONSTANTS_H
#define CONSTANTS_H

#include <iostream>
#include <unordered_map>
#include <vector>
#include <string>
#include <utility>

using namespace std;

typedef pair<int,int> LineColumnPair;
typedef vector<LineColumnPair> OccuranceVector;  
typedef unordered_map<string, OccuranceVector> Table;

const string INPUT_FILE = "input_files/source_code_example.txt"; 
const string OUTPUT_FILE = "output_files/parse.txt"; 

const string GENERIC_TOKEN = "OUTRO";
const string IDENTIFIER_TOKEN = "IDENT";
const string INTEGER_TOKEN = "NI";
const string FLOAT_TOKEN = "NPF";
const string STRING_TOKEN = "A DEFINIR STRINGTOKEN"; // Change it soon.
enum DiagramProcessing {  
    IN_PROGRESS,  
    FINISHED,
    FINISHED_AND_BACKTRACK,
    FAILED
};

#endif