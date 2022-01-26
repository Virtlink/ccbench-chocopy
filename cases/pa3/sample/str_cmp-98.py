a:str = "Hello"
b:str = "World"
c:str = "ChocoPy"

def eq(a:str, b:str) -> bool:
    return a == b

def neq(a:str, b:str) -> bool:
    return a != b

print(eq(a,a))
[[Statement]]
print(neq(a,b))
print(neq(b,b))
print(eq(c,a))
print(neq(c,b))

