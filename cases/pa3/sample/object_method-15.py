class A(object):
    a:int = $INT

    def foo(self:"A", ignore:object) -> int:
        return self.a

class B(A):
    b:bool = True

    def __init__(self:"B"):
        print("B")

    def bar(self:"B") -> int:
        return self.foo(self.b)

print(B().bar())
