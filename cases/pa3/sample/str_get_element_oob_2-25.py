x:str = "abc"
a:str = ""

def str_get(s:$ID, i:int) -> str:
    return s[i]

a = str_get(x, 3)
print(a)
