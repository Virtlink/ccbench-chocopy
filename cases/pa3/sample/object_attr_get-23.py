class A(object):
    a:int = 42

class B(A):
    $VarDef

    def __init__(self:"B"):
        print("B")

a:A = None
b:B = None

a = b = B()
print(a.a)
print(b.a)
print(b.b)
