class A(object):
    a:int = 42

class B(A):
    b:bool = True

    def __init__(self:"B"):
        $Exp

a:A = None
b:B = None

a = b = B()
b.a = 1
b.b = False
print(a.a)
print(b.a)
print(b.b)
