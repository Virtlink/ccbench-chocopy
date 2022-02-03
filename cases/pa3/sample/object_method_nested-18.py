class A(object):
    a:int = 42

    def $ID(self:"A", ignore:object) -> int:
        return self.a

class B(A):
    b:bool = True

    def __init__(self:"B"):
        print("B")

    def bar(self:"B") -> int:
        def qux(p: bool) -> int:
            return self.foo(p)
        return qux(True)

print(B().bar())
