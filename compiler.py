from ctypes import CFUNCTYPE, c_double

import llvmlite.binding as llvm

llvm.initialize()
llvm.initialize_native_target()
llvm.initialize_native_asmprinter()

llvm_ir = """
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
   """

def create_execution_engine():
    # Create a target machine representing the host
    target = llvm.Target.from_default_triple()
    target_machine = target.create_target_machine()
    # And an execution engine with an empty backing module
    backing_mod = llvm.parse_assembly("")
    engine = llvm.create_mcjit_compiler(backing_mod, target_machine)
    return engine


def compile_ir(engine, llvm_ir):
    """
    Compile the LLVM IR string with the given engine.
    The compiled module object is returned.
    """
    # Create a LLVM module object from the IR
    mod = llvm.parse_assembly(llvm_ir)
    mod.verify()
    # Now add the module and make sure it is ready for execution
    engine.add_module(mod)
    engine.finalize_object()
    engine.run_static_constructors()
    return mod


engine = create_execution_engine()
mod = compile_ir(engine, llvm_ir)

func_ptr_add = engine.get_function_address("fpadd")
func_ptr_sub = engine.get_function_address("fpsub")
cfunc_add = CFUNCTYPE(c_double, c_double, c_double)(func_ptr_add)
cfunc_sub = CFUNCTYPE(c_double, c_double, c_double)(func_ptr_sub)

print(mod)

class Compiler:
    def compile(self, nodes):
        for node in nodes:
            if node.type == "EXPR":
                if node.op == "PLUS":
                    res = cfunc_add(float(node.left), float(node.right))
                    print(res)

                elif node.op == "MINUS":
                    res = cfunc_sub(float(node.left), float(node.right))
                    print(res)

