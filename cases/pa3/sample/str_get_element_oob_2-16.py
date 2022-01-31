x:str = "abc"
a:str = $Literal

def str_get(s:str, i:int) -> str:
    return s[i]

a = str_get(x, 3)
print(a)
