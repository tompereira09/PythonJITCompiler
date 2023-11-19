class Token:
    def __init__(self, ty, value):
        self.ty = ty
        self.value = value
        self.end_pos = 0


def nth(n: int, src: str):
    if n < len(src):
        return src[n]
    else:
        return '\0'


def get_next(n: int, src: str):
    return nth(n + 1, src)


def is_ident_char(c: str, first: bool):
    if first:
        if c.isalpha():
            return True
        else:
            return False
    else:
        if c.isalpha() or c == "_" or c.isalnum():
            return True
        else:
            return False


def clearToken(token: Token):
    token.ty = None
    token.value = None
    token.start_pos = 0
    token.end_pos = 0


class Tokenizer:
    def tokenize(self, src: str, pos : int):
        c = nth(pos, src)
        if c == "+":
            #print("+")
            obj = Token("PLUS", None)
            obj.end_pos = pos + 1
            return obj

        if c.isnumeric():
            #print(c)
            end = pos
            while c.isnumeric():
                end += 1
                c = nth(end, src)
            obj = Token("INT", src[pos:end])
            obj.end_pos = end
            #print(obj.end_pos)
            return obj

        if c == " ":
            obj = Token("BLANK", None)
            obj.end_pos = pos + 1
            return obj

        if pos <= len(src):
            obj = Token("EOF", None)
            obj.end_pos = pos + 1
            return obj


