#ifndef FLOAT_CONST_DIAGRAM_H
#define FLOAT_CONST_DIAGRAM_H

#include "constants.h"
#include "diagram.h"

class FloatConstDiagram: public Diagram {
  public:
    std::pair<DiagramProcessing, std::pair<std::string, std::string>> parse(const char entry);
  
};

#endif