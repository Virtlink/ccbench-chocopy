class A(object):
    a:int = 42

    def foo(self:"A", ignore:object) -> int:
        return self.a

[[Definition]]

print(B().bar())
