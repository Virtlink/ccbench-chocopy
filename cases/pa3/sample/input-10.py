# Test of 'input' function.

s: str = ""

$AssignTarget input()
while len(s) > 0:
    print(s)
    s = input()
