class Compiler:
    def __init__(self):
        self.ops = {"PLUS":"add", "MINUS":"sub"}
    def compile(self, nodes):
        file = open("main.asm", "w")
        for node in nodes:
            if node.type == "EXPR":
                file.write(f'mov eax, {node.left}\n')
                file.write(f'mov ebx, {node.right}\n')
                file.write(f'{self.ops[node.op]} eax, ebx\n\n')

