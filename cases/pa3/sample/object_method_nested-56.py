class A(object):
    a:int = 42

    def foo(self:"A", ignore:object) -> int:
        return self.a

class B(A):
    b:bool = True

    [[FuncDef]]

    def bar(self:"B") -> int:
        def qux(p: bool) -> int:
            return self.foo(p)
        return qux(True)

print(B().bar())