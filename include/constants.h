#ifndef CONSTANTS_H
#define CONSTANTS_H

#include <iostream>
#include <string>

const std::string GENERIC_TOKEN = "OUTRO";
const std::string IDENTIFIER_TOKEN = "IDENT";
const std::string INTEGER_TOKEN = "NI";
const std::string FLOAT_TOKEN = "NPF";
const std::string STRING_TOKEN = "A DEFINIR STRINGTOKEN"; // Change it soon.
enum DiagramProcessing {  
    IN_PROGRESS,  
    FINISHED,
    FINISHED_AND_BACKTRACK,
    FAILED
};

#endif