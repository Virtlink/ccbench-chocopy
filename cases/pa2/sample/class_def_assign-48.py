class A(object):
    x:int = 1

class B(A):
    def __init__(self: "B"):
        pass

class C(B):
    z:bool = [[Literal]]

a:A = None
b:B = None
c:C = None

a = A()
a = B()
b = a = c = C()
c = None
