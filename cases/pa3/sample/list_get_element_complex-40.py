next:int = 0

def next_int() -> int:
    global next
    next = next + 1
    return next

$FuncDef

print(make_list()[next_int() - 3])
