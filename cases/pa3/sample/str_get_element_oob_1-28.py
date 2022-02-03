x:str = "abc"
a:str = ""

def str_get(s:str, i:$Type) -> str:
    return s[i]

a = str_get(x, -1)
print(a)
