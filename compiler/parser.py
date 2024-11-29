class Parser:
    def __init__(self, input_file_path: str):
        self.line_number = 1
        self.column_number = 0
        self.character_to_backtrack = ''
        self.input_file_path = input_file_path
        self.file = None

    def open_file(self):
        try:
            self.file = open(self.input_file_path, 'r')
        except IOError:
            print("Error opening input file!")
            return False
        return True

    def close_file(self):
        if self.file:
            self.file.close()

    def get_next_char(self):
        # Verifica se há um caractere a ser retrocedido
        if self.character_to_backtrack:
            c = self.character_to_backtrack
            self.character_to_backtrack = ''
            return c

        c = self.file.read(1)

        if c:
            self.column_number += 1
            if c == '\n':
                self.line_number += 1
                self.column_number = 0

        return c

    def backtrack(self, c: str):
        self.character_to_backtrack = c
        # Retrocede o ponteiro do arquivo
        self.file.seek(self.file.tell() - 1)
        if c == '\n':
            self.line_number -= 1
            self.column_number = 0  # Considerando que voltamos para o início da linha anterior
        else:
            self.column_number -= 1

    def get_line_number(self):
        return self.line_number

    def get_column_number(self):
        return self.column_number
