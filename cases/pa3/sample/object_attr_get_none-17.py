class A(object):
    a:int = 42

$ClassDef

a:A = None
b:B = None

a = B()
print(a.a)
print(b.a)
print(b.b)
