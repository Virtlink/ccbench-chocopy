next:int = 0

def next_int() -> int:
    global next
    next = next + 1
    return next

def [[ID]]() -> [int]:
    return [next_int(), next_int(), next_int()]

print(make_list()[next_int() - 3])
