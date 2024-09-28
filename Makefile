CXX := g++
CXXFLAGS := -Wall -Wextra -std=c++17

SRC_DIR := src
INC_DIR := include
BUILD_DIR := build
TARGET := main.out

SRC_FILES := $(wildcard $(SRC_DIR)/*.cpp)
OBJ_FILES := $(patsubst $(SRC_DIR)/%.cpp,$(BUILD_DIR)/%.o,$(SRC_FILES))
INC_FILES := $(wildcard $(INC_DIR)/*.h)

all: $(TARGET)

$(BUILD_DIR)/%.o: $(SRC_DIR)/%.cpp $(INC_FILES)
	@mkdir -p $(BUILD_DIR)
	$(CXX) $(CXXFLAGS) -I$(INC_DIR) -c $< -o $@

$(TARGET): $(OBJ_FILES)
	$(CXX) $(CXXFLAGS) $^ -o $@

clean:
	rm -rf $(BUILD_DIR) $(TARGET)

run:
	./$(TARGET)

.PHONY: all clean
