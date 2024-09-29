#ifndef STRING_CONST_DIAGRAM_H
#define STRING_cONST_DIAGRAM_H

#include "constants.h"
#include "diagram.h"

class StringConstDiagram: Diagram {
  public:
    std::pair<DiagramProcessing, std::pair<std::string, std::string>> parse(const char entry);
  
};

#endif