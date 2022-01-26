x:str = ""
[[VarDef]]
z:str = "abc"

for x in z:
    print(x)
    for x in "":
        print(x)
