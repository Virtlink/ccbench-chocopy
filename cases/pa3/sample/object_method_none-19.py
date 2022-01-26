class A(object):
    a:int = 42

    def foo() -> int:
        return self.a

class B(A):
    b:bool = True

    def __init__(self:"B"):
        print("B")

    def bar(self:"B") -> int:
        a:A = None
        return a.foo(self.b)

print(B().bar())
