class A(object):
    a:int = 42

class B(A):
    $ClassBody

a:A = None
b:B = None

a = B()
print(a.a)

b.a = 1
b.b = False
print(b.a)
print(b.b)
