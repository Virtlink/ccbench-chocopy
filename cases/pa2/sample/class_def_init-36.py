class A(object):
    x:int = 1

class B(A):
    def __init__(self: "B"):
        pass

[[Definition]]

a:A = None
b:B = None
c:C = None

a = A()
b = B()
c = C()
