x:int = 0
$TypedVar = 0
z:[int] = None
e:[int] = None

z = [1,2,3]
e = []

for x in z:
    for y in e:
        print("Never")
    print(x)
