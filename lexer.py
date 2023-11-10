class Token:
    def __init__(self):
        self.ty = None
        self.value = None
        self.start_pos = 0
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
    def __init__(self):
        self.token_obj = Token()

    def tokenize(self, src: str):
        clearToken(self.token_obj)
        pos = 0
        c = nth(pos, src)
        if is_ident_char(c, True):
            start = pos
            while is_ident_char(get_next(pos, src), False):
                pos += 1
            end = pos + 1
            self.token_obj.ty = "IDENT"
            self.token_obj.value = src[start:end]
            self.token_obj.end_pos = end
            return self.token_obj

        if c.isnumeric():
            start = pos
            while get_next(pos, src).isnumeric():
                pos += 1
            end = pos + 1
            self.token_obj.ty = "NUMBER"
            self.token_obj.value = src[start:end]
            self.token_obj.end_pos = end
            return self.token_obj

        if c == "'" or c == '"':
            start = pos + 1
            while get_next(pos, src) != "'" and get_next(pos, src) != '"':
                if pos >= len(src):
                    print("Unfinished String"),
                    quit()
                pos += 1
            end = pos + 1

            self.token_obj.ty = "STR"
            self.token_obj.value = src[start:end]
            self.token_obj.end_pos = end + 1
            return self.token_obj

        if c == " ":
            self.token_obj.ty = "BLANK"
            self.token_obj.end_pos = pos + 1
            return self.token_obj

        if c == "(":
            self.token_obj.ty = "LPAREN"
            self.token_obj.end_pos = pos + 1
            return self.token_obj

        if c == ")":
            self.token_obj.ty = "RPAREN"
            self.token_obj.end_pos = pos + 1
            return self.token_obj

        if c == "\0":
            self.token_obj.ty = "EOF"
            self.token_obj.end_pos = pos + 1
            return self.token_obj

        if c == "+":
            if get_next(pos, src) == "=":
                self.token_obj.ty = "PLUS_EQ"
                self.token_obj.end_pos = pos + 2
                return self.token_obj
            self.token_obj.ty = "PLUS"
            self.token_obj.end_pos = pos + 1
            return self.token_obj

        if c == "-":
            if get_next(pos, src) == "=":
                self.token_obj.ty = "MINUS_EQ"
                self.token_obj.end_pos = pos + 2
                return self.token_obj
            self.token_obj.ty = "MINUS"
            self.token_obj.end_pos = pos + 1
            return self.token_obj

        if c == "/":
            if get_next(pos, src) == "=":
                self.token_obj.ty = "DIV_EQ"
                self.token_obj.end_pos = pos + 2
                return self.token_obj
            self.token_obj.ty = "DIV"
            self.token_obj.end_pos = pos + 1
            return self.token_obj

        if c == "*":
            if get_next(pos, src) == "=":
                self.token_obj.ty = "MUL_EQ"
                self.token_obj.end_pos = pos + 2
                return self.token_obj
            self.token_obj.ty = "MUL"
            self.token_obj.end_pos = pos + 1
            return self.token_obj

        if c == "=":
            if get_next(pos, src) == "=":
                self.token_obj.ty = "DOUBLE_EQ"
                self.token_obj.end_pos = pos + 2
                return self.token_obj
            self.token_obj.ty = "EQ"
            self.token_obj.end_pos = pos + 1
            return self.token_obj

        if c == ">":
            if get_next(pos, src) == "=":
                self.token_obj.ty = "GREATER_EQ"
                self.token_obj.end_pos = pos + 2
                return self.token_obj

            if get_next(pos, src) == ">":
                self.token_obj.ty = "DOUBLE_GREATER"
                self.token_obj.end_pos = pos + 2
                return self.token_obj

            self.token_obj.ty = "GREATER"
            self.token_obj.end_pos = pos + 1
            return self.token_obj

        if c == "<":
            if get_next(pos, src) == "=":
                self.token_obj.ty = "SMALLER_EQ"
                self.token_obj.end_pos = pos + 2
                return self.token_obj

            if get_next(pos, src) == "<":
                self.token_obj.ty = "DOUBLE_SMALLER"
                self.token_obj.end_pos = pos + 2
                return self.token_obj

            self.token_obj.ty = "SMALLER"
            self.token_obj.end_pos = pos + 1
            return self.token_obj
