x:str = "abc"
a:str = ""

def str_get(s:str, i:int) -> str:
    return s[i]

a = $Var(x, 3)
print(a)
