class A(object):
    a:int = 42

class B(A):
    b:bool = True

    def __init__(self:"B"):
        print($STRING)

a:A = None
b:B = None

a = B()
print(a.a)

b.a = 1
b.b = False
print(b.a)
print(b.b)
