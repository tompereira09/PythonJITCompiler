####### IMPORTS
from lexer import *
###############


tokens = []
tokenizer = Tokenizer()
inpstr = "123 + 23 + 1"
inpoint = 0
obj = tokenizer.tokenize(inpstr, inpoint)
#print(obj.ty, obj.value)
tokens.append(obj)
inpoint = obj.end_pos
while obj.ty != "EOF":
    obj = tokenizer.tokenize(inpstr, inpoint)
    #print(obj.ty, obj.value)
    tokens.append(obj)
    inpoint = obj.end_pos

for i in tokens:
    print(i.ty, i.value)

