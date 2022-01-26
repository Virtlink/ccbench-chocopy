# Test of 'input' function.

s: [[Type]] = ""

s = input()
while len(s) > 0:
    print(s)
    s = input()
