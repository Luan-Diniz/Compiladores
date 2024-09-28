#ifndef CONSTANTS_H
#define CONSTANTS_H

#include <iostream>
#include <string>

const std::string GENERIC_TOKEN = "OUTRO";
const std::string IDENTIFIER_TOKEN = "IDENT";
const std::string INTEGER_TOKEN = "NI";
const std::string FLOAT_TOKEN = "NPF";

enum DiagramProcessing {  
    IN_PROGRESS,  
    FINISHED,
    FINISHED_AND_BACKTRACK,
    FAILED
};

#endif