x:int = 0
z:[int] = None

z = [$Literal, 2, 1]

for x in z:
    z[x] = x
    print(x)
