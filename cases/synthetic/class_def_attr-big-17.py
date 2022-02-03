class A(object):
    x:int = 1

$ClassDef

class A3(object):
    x:int = 1
    x2:int = 1
    x3:int = 1

class A4(object):
    x:int = 1
    x2:int = 1
    x3:int = 1
    x4:int = 1

class A5(object):
    x:int = 1
    x2:int = 1
    x3:int = 1
    x4:int = 1
    x5:int = 1

class B(A):
    def __init__(self: "B"):
        pass

class B2(A):
    def __init__(self: "B2"):
        pass

class B3(A):
    def __init__(self: "B3"):
        pass

class B4(A):
    def __init__(self: "B4"):
        pass

class B5(A):
    def __init__(self: "B5"):
        pass

class C(B):
    z:bool = True

class C2(B):
    z:bool = True
    z2:bool = True

class C3(B):
    z:bool = True
    z2:bool = True
    z3:bool = True

class C4(B):
    z:bool = True
    z2:bool = True
    z3:bool = True
    z4:bool = True

class C5(B):
    z:bool = True
    z2:bool = True
    z3:bool = True
    z4:bool = True
    z5:bool = True

a:A = None
a2:A = None
a3:A = None
a4:A = None
a5:A = None
b:B = None
b2:B = None
b3:B = None
b4:B = None
b5:B = None
c:C = None
c2:C = None
c3:C = None
c4:C = None
c5:C = None

a = A()
a2 = A()
a3 = A()
a4 = A()
a5 = A()
b = B()
b2 = B()
b3 = B()
b4 = B()
b5 = B()
c = C()
c2 = C()
c3 = C()
c4 = C()
c5 = C()

a.x = 1
b.x = a.x
c.z = a.x == b.x

