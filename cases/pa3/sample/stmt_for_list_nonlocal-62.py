x:int = 0
def crunch(zz:[[int]]) -> object:
    z:[int] = None
    global x
    def make_z() -> object:
        nonlocal z
        for z in zz:
            pass # Set z to last element in zz

    make_z()
    for x in z:
        pass # Set x to last element in z

$Exp
print(x) 
