class A(object):
    x:int = 1

$ClassDef

class C(B):
    z:bool = True

a:A = None
b:B = None
c:C = None

a = A()
b = B()
c = C()
