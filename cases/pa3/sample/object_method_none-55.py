class A(object):
    a:int = 42

    def foo(self:"A", ignore:object) -> int:
        return self.a

class B(A):
    b:bool = True

    $ClassBodyMember

    def bar(self:"B") -> int:
        a:A = None
        return a.foo(self.b)

print(B().bar())
