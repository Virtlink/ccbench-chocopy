class A(object):
    a:int = 42

class B(A):
    $ClassBody

a:A = None
b:B = None

a = b = B()
b.a = 1
b.b = False
print(a.a)
print(b.a)
print(b.b)
