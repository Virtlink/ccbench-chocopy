x:int = 0
y:int = 0
z:[int] = None

z = [1, 2, $INT]

for x in z:
    for y in z:
        print(x * y)
