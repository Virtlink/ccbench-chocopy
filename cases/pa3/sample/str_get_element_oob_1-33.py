x:str = "abc"
a:str = ""

def str_get(s:str, i:int) -> str:
    $FuncBody

a = str_get(x, -1)
print(a)
