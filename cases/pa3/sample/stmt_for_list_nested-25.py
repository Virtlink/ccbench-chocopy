x:int = 0
y:int = 0
z:[int] = $Literal

z = [1, 2, 3]

for x in z:
    for y in z:
        print(x * y)
