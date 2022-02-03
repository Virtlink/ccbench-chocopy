x:str = ""
y:str = "123"
z:str = "abc"

for x in z:
    $Var(x)
    for x in y:
        print(x)
