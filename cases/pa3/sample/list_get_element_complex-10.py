next:int = 0

$FuncDef

def make_list() -> [int]:
    return [next_int(), next_int(), next_int()]

print(make_list()[next_int() - 3])
