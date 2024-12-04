PYTHON := python3
PIP := pip3
VENV_DIR := venv
SRC_DIR := compiler
OUT_DIR := $(SRC_DIR)/outputs
REQ_FILE := requirements.txt
TARGET := main.py

.PHONY: all run install-deps clean venv

# Tarefa padrão
all: run

# Criar ambiente virtual
venv:
	$(PYTHON) -m venv $(VENV_DIR)

# Instalar dependências no ambiente virtual
install-deps: venv
	$(VENV_DIR)/bin/$(PIP) install -r $(REQ_FILE)

# Executar o programa principal dentro do ambiente virtual
run: install-deps
	$(VENV_DIR)/bin/$(PYTHON) $(SRC_DIR)/$(TARGET)

# Limpar ambiente virtual e arquivos temporários
clean:
	rm -rf $(VENV_DIR)
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find $(OUT_DIR) -type f ! -name ".gitkeep" -exec rm -f {} +

