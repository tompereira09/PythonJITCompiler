import lexer
import parser
import compiler
import os

file = open(input("filename > "), "r")
nodes = []
conts = file.readlines()
for i in conts:
    #print(i)
    lex = lexer.Lexer()
    tokens = []
    strtt = i
    for i in range(len(strtt)):
        if strtt != "":
            obj = lex.tokenize(strtt)
            #print(obj.token_ty, obj.val, obj.len)
            if obj.token_ty != "BLANK":
                tokens.append(obj)

            strtt = strtt[obj.len:]



    par = parser.Parser()
    pobj = par.parse(tokens)
    print(pobj.left, pobj.op, pobj.right)
    nodes.append(pobj)

cmp = compiler.Compiler()
cmp.compile(nodes)
os.system("nasm main.asm")