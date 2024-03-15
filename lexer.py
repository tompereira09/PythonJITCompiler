class LexToken:
    def __init__(self, ty, val, len):
        self.token_ty = ty
        self.val = val
        self.len = len


class Lexer:
    def __init__(self):
        self.ops = {"+":"PLUS", "-":"MINUS", "/":"DIV", "*":"MUL"}

    def isident(self, char, first):
        if first:
            if char.isalpha() or char == "_":
                return True
            else:
                return False
        else:
            if char.isalpha() or char.isalnum() or char == "_":
                return True
            else:
                return False

    def tokenize(self, str_tt):
        for char_ptr in range(len(str_tt)):
            if str_tt[char_ptr] in self.ops:
                return LexToken(self.ops[str_tt[char_ptr]], None, 1)
            
            elif self.isident(str_tt[char_ptr], True):
                ptr = 1
                while ptr <= len(str_tt) - 1 and self.isident(str_tt[ptr], False):
                    ptr += 1
    
                
                val = str_tt[0:ptr]
                return LexToken("IDENT", val, ptr)

            elif str_tt[char_ptr].isnumeric():
                ptr = 1
                while ptr <= len(str_tt) - 1 and str_tt[ptr].isnumeric():
                    ptr += 1
    
                
                val = str_tt[0:ptr]
                return LexToken("NUMBER", val, ptr)

            elif str_tt[char_ptr] == " " or str_tt[char_ptr] == "\n":
                return LexToken("BLANK", None, 1)
