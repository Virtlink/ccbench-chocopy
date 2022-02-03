x:str = "abc"
a:str = ""

def str_get(s:str, i:int) -> str:
    return $ID[i]

a = str_get(x, -1)
print(a)
