tk = [1, "+", 2, "-", 3]

class parser:
    def parse(self, tks, ptr):
        left = tks[ptr]
        op = tks[ptr+1]
        try:
            if tks[ptr+3] != None:
                right = self.parse(tks, 2)
                return (left, op, right)
        except:
            right = tks[ptr+2]
            return (left, op, right)

p = parser()
print(p.parse(tk, 0))
