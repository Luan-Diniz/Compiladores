#ifndef INT_CONST_DIAGRAM_H
#define INT_CONST_DIAGRAM_H

#include "constants.h"
#include "diagram.h"

class IntConstDiagram: public Diagram {
  public:
    std::pair<DiagramProcessing, std::pair<std::string, std::string>> parse(const char entry);
  
};

#endif