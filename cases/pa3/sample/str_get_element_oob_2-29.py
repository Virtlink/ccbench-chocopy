x:str = "abc"
a:str = ""

def str_get(s:str, i:$ID) -> str:
    return s[i]

a = str_get(x, 3)
print(a)
