x:int = 0
y:int = 0
[[VarDef]]
e:[int] = None

z = [1,2,3]
e = []

for x in z:
    for y in e:
        print("Never")
    print(x)
