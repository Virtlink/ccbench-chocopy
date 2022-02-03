x:int = 0
z:[int] = None

z = [1, $Literal, 1]

for x in z:
    z[x] = x
    print(x)
