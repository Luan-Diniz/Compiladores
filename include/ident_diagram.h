#ifndef IDENT_DIAGRAM_H
#define IDENT_DIAGRAM_H

#include "constants.h"
#include "diagram.h"

class IdentDiagram: public Diagram {
  public:
    std::pair<DiagramProcessing, std::pair<std::string, std::string>> parse(const char entry);
  
};

#endif