class A(object):
    x:$ID = 1

class B(A):
    def __init__(self: "B"):
        pass

class C(B):
    z:bool = True

a:A = None
b:B = None
c:C = None

a = A()
b = B()
c = C()
