class A(object):
    a:int = 42

    def foo(self:"A", ignore:object) -> int:
        return self.a

class B(A):
    b:bool = True

    def __init__(self:"B"):
        print("B")

    def bar(self:"[[ID]]") -> int:
        return self.foo(self.b)

print(B().bar())
