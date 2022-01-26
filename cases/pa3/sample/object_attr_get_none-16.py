class A(object):
    a:int = 42

[[Definition]]

a:A = None
b:B = None

a = B()
print(a.a)
print(b.a)
print(b.b)
