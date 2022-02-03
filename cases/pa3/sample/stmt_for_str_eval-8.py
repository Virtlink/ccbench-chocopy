x:str = $Literal
z:str = "abc"

for x in z:
    z = "doesn't matter"
    print(x)
