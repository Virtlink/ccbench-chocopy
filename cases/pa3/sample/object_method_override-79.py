class A(object):
    a:int = 42

    def foo(self:"A", ignore:object) -> int:
        return self.a

class B(A):
    b:bool = True

    def __init__(self:"B"):
        print("B")

    [[FuncDef]]

    def foo(self:"B", ignore:object) -> int:
        return 1

print(B().bar())
