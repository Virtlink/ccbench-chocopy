x:str = "abc"
a:str = ""

def str_get(s:str, i:int) -> str:
    return s[i]

a = str_get(x, -$Exp)
print(a)
