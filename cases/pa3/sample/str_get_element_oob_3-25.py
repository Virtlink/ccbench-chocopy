x:str = ""
a:str = ""

def str_get(s:$ID, i:int) -> str:
    return s[i]

a = str_get(x, 0)
print(a)
