class A(object):
    x:int = 1

class B(A):
    def __init__(self: "B"):
        pass

class C(B):
    [[ClassBody]]

a:A = None
b:B = None
c:C = None

a = A()
b = B()
c = C()