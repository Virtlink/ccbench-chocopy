class A(object):
    [[ClassBody]]

class B(A):
    b:bool = True

    def __init__(self:"B"):
        print("B")

    def bar(self:"B") -> int:
        return self.foo(self.b)

print(B().bar())
