class A(object):
    a:int = 42

    def foo(self:"A", ignore:object) -> int:
        return self.a

class B(A):
    b:bool = True

    $ClassBodyMember

    def bar(self:"B") -> int:
        return self.foo(self.b)

    def foo(self:"B", ignore:object) -> int:
        return 1

print(B().bar())
