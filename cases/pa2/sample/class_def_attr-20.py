class A(object):
    x:int = 1

class B(A):
    [[ClassBody]]

class C(B):
    z:bool = True

a:A = None
b:B = None
c:C = None

a = A()
b = B()
c = C()

a.x = 1
b.x = a.x
c.z = a.x == b.x
