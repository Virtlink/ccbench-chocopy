x:str = "abc"
a:str = ""

def str_get(s:str, i:int) -> str:
    return $Var[i]

a = str_get(x, 3)
print(a)
