from ctypes import CFUNCTYPE, c_double

import llvmlite.binding as llvm

llvm.initialize()
llvm.initialize_native_target()
llvm.initialize_native_asmprinter()

bultins = """
   ; ModuleID = "Compiler"
   target triple = "unknown-unknown-unknown"
   target datalayout = ""

   define double @"fpadd"(double %".1", double %".2")
   {
   entry:
     %"res" = fadd double %".1", %".2"
     ret double %"res"
   }

   define double @"fpsub"(double %".1", double %".2")
   {
   entry:
     %"res" = fsub double %".1", %".2"
     ret double %"res"
   }

   define double @"fpmul"(double %".1", double %".2")
   {
   entry:
     %"res" = fmul double %".1", %".2"
     ret double %"res"
   }

   define double @"fpdiv"(double %".1", double %".2")
   {
   entry:
     %"res" = fdiv double %".1", %".2"
     ret double %"res"
   }
   """

def create_execution_engine():
    # Create a target machine representing the host
    target = llvm.Target.from_default_triple()
    target_machine = target.create_target_machine()
    # And an execution engine with an empty backing module
    backing_mod = llvm.parse_assembly("")
    engine = llvm.create_mcjit_compiler(backing_mod, target_machine)
    return engine


def compile_ir(engine, bultins):
    # Create a LLVM module object from the IR
    mod = llvm.parse_assembly(bultins)
    mod.verify()
    # Now add the module and make sure it is ready for execution
    engine.add_module(mod)
    engine.finalize_object()
    engine.run_static_constructors()
    return mod


engine = create_execution_engine()
mod = compile_ir(engine, bultins)

func_ptr_add = engine.get_function_address("fpadd")
func_ptr_sub = engine.get_function_address("fpsub")
func_ptr_mul = engine.get_function_address("fpmul")
func_ptr_div = engine.get_function_address("fpdiv")
cfunc_add = CFUNCTYPE(c_double, c_double, c_double)(func_ptr_add)
cfunc_sub = CFUNCTYPE(c_double, c_double, c_double)(func_ptr_sub)
cfunc_mul = CFUNCTYPE(c_double, c_double, c_double)(func_ptr_mul)
cfunc_div = CFUNCTYPE(c_double, c_double, c_double)(func_ptr_div)

print("----------------------BULTINS----------------------")
print(mod)
print("----------------------BULTINS----------------------")

class Compiler:
    def compile(self, nodes):
        for node in nodes:
            if node.type == "EXPR":
                if node.op == "PLUS":
                    res = cfunc_add(float(node.left.rawval), float(node.right.rawval))
                    print(res)

                elif node.op == "MINUS":
                    res = cfunc_sub(float(node.left.rawval), float(node.right.rawval))
                    print(res)

                elif node.op == "MUL":
                    res = cfunc_mul(float(node.left.rawval), float(node.right.rawval))
                    print(res)

                elif node.op == "DIV":
                    res = cfunc_div(float(node.left.rawval), float(node.right.rawval))
                    print(res)
