import lexer

class ParseToken:
    def __init__(self, rawval, ty):
        self.rawval = rawval
        self.type = ty
        self.len = 0
        self.left = None
        self.right = None

class ExprToken:
    def __init__(self, ty, left, right):
        self.type = ty
        self.len = 0
        self.op = None

class FnToken:
    def __init__(self, args):
        self.type = "FN"
        self.builtin = False
        self.name = ""
        self.args = args
        self.len = 0

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
                self.currexpr.left = ParseToken(self.tokens[currtoken_ptr].val, "NUM")
                self.currexpr.op = self.tokens[currtoken_ptr + 1].token_ty
                if self.tokens[currtoken_ptr + 2].token_ty == "NUMBER":
                    self.currexpr.right = ParseToken(self.tokens[currtoken_ptr + 2].val, "NUM")
                    self.currexpr.len = 3
                    return self.currexpr
                elif self.tokens[currtoken_ptr + 2].token_ty == "EXPR":
                    pass # WIP
                else:
                    raise Exception(f'Expected \'NUMBER\' or \'EXPR\', got: \'{self.tokens[currtoken_ptr + 2].token_ty}\'.')
        elif self.tokens[currtoken_ptr].token_ty == "IDENT":
            if self.tokens[currtoken_ptr].val == "fib":
                if self.tokens[currtoken_ptr + 1].token_ty == "LPAREN":
                    if self.tokens[currtoken_ptr + 2].token_ty == "NUMBER":
                        if self.tokens[currtoken_ptr + 3].token_ty == "RPAREN":
                            tk = FnToken([self.tokens[currtoken_ptr + 2]])
                            tk.len = 4
                            tk.builtin = True
                            tk.name = "FIB"

                            return tk
                        else:
                            raise Exception(f'Expected \'RPAREN\', got: \'{self.tokens[currtoken_ptr + 3].token_ty}\'.')
                    else:
                        raise Exception(f'Expected \'NUMBER\', got: \'{self.tokens[currtoken_ptr + 2].token_ty}\'.')
                else:
                    raise Exception(f'Expected \'LPAREN\', got: \'{self.tokens[currtoken_ptr + 1].token_ty}\'.')
            else:
                raise Exception(f'Ident not implemented \'{self.tokens[currtoken_ptr].val}\'.')





