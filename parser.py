# IMPORTS
import lexer

tokens = []

tokenizer = lexer.Tokenizer()
input_string = "1 + 2"
obj = tokenizer.tokenize(input_string)
tokens.append(obj)
while obj.ty != "EOF":
    input_string = input_string[obj.end_pos:]
#    print(obj.ty, obj.value)
    tokens.append(obj)
    obj = tokenizer.tokenize(input_string)

class NumberToken:
    def __init__(self, tok):
        self.tok = tok

    def __repr__(self):
        return f'{self.tok.value}'

class OpToken:
    def __init__(self):
        self.op = ""
        self.left = None
        self.right = None

    def __repr__(self):
        return f'({self.left} {self.op} {self.right})'
