class A(object):
    x:int = 1

class B(A):
    def __init__(self: "B"):
        pass

class C(B):
    z:bool = True

a:A = None
[[ID]]:B = None
c:C = None

a = A()
b = B()
c = C()
