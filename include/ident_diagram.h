#ifndef IDENT_DIAGRAM_H
#define IDENT_DIAGRAM_H

#include <iostream>
#include <string>
#include <ctype.h>
#include <cassert>

#include "constants.h"
#include "diagram.h"

class IdentDiagram: Diagram {
  public:
    std::pair<DiagramProcessing, std::pair<std::string, std::string>> parse(const char entry);
  
};

#endif