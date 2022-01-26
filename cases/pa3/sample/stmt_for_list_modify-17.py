x:int = 0
z:[int] = [[Literal]]

z = [1, 2, 1]

for x in z:
    z[x] = x
    print(x)
