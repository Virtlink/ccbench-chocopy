class A(object):
    a:int = 42

class B(A):
    

a:A = None
b:B = None

a = B()
print(a.a)
print(b.a)
print(b.b)
