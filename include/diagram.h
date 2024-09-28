#ifndef DIAGRAM_H
#define DIAGRAM_H

#include <iostream>
#include <string>
#include <ctype.h>
#include <cassert>

#include "constants.h"

class Diagram {

  /*
  First:
      IN_PROGRESS: It is processing the token.
      FAILED: The Diagram has not accepted the entries.
      FINISHED: Has completed the token processment (it was accepted).
      FINISHED_AND_BACKTRACK: Has completed the token processment (it was accepted)
      and the pointer should backtrack one character.
  Second:
      First:
          When the processment has been completed, stores the token.
      Second:
          Stores the lexem.
  */
  public:
    virtual std::pair<DiagramProcessing,
      std::pair<std::string, std::string>> parse(const char entry) = 0;

  protected:
    void reset();
  
  protected:
    int _current_state = 0;
    std::string _current_lexem = "";

};

#endif