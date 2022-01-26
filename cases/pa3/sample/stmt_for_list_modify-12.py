x:int = 0
[[TypedVar]] = None

z = [1, 2, 1]

for x in z:
    z[x] = x
    print(x)
