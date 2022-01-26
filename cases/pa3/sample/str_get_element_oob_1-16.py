x:str = "abc"
a:str = [[Literal]]

def str_get(s:str, i:int) -> str:
    return s[i]

a = str_get(x, -1)
print(a)
