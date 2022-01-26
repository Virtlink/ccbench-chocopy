class A(object):
    a:int = 42

class B(A):
    b:bool = True

    [[ClassBodyMember]]

a:A = None
b:B = None

a = B()
print(a.a)

b.a = 1
b.b = False
print(b.a)
print(b.b)
