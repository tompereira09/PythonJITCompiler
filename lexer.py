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


class Tokenizer:
    def __init__(self):
        self.token_obj = Token()

    def tokenize(self, src: str):
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

        if c == "'" or c == '"':
            start = pos + 1
            while get_next(pos, src) != "'" and get_next(pos, src) != '"':
                pos += 1
            end = pos + 2

            self.token_obj.ty = "STR"
            self.token_obj.value = src[start:end]
            self.token_obj.end_pos = end
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


tokenizer = Tokenizer()
input_string = "print('hello')"
obj = tokenizer.tokenize(input_string)
while obj.ty != "EOF":
    input_string = input_string[obj.end_pos:]
    print(obj.ty, obj.value)
    obj = tokenizer.tokenize(input_string)
