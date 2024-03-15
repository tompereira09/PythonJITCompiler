import lexer

class ParseToken:
    def __init__(self, rawval, ty, left, right):
        self.rawval = rawval
        self.type = ty
        self.len = 0

class ExprToken:
    def __init__(self, ty, left, right):
        self.type = ty
        self.len = 0
        self.op = None

class Parser:
    def __init__(self):
        self.tokens = None
        self.currexpr = ExprToken("EXPR", None, None)
        self.ops = ["PLUS", "MINUS", "MUL", "DIV"]
        self.nodes = []

    def parse(self, tokens):
        self.tokens = tokens
        currtoken_ptr = 0
        if self.tokens[currtoken_ptr].token_ty == "NUMBER":
            if self.tokens[currtoken_ptr + 1].token_ty in self.ops:
                self.currexpr.left = self.tokens[currtoken_ptr].val
                self.currexpr.op = self.tokens[currtoken_ptr + 1].token_ty
                if self.tokens[currtoken_ptr + 2].token_ty == "NUMBER":
                    self.currexpr.right = self.tokens[currtoken_ptr + 2].val
                    self.currexpr.len = 3
                    return self.currexpr



