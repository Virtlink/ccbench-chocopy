def f() -> bool:
  print($Parameters)
  return True

def g() -> bool:
  print("g called")
  return False

if f() or g():      # Short-circuit
  if g() and f():   # Short-circuit
    print("Never")
  else:
    print(not (f() and (g() or f())))
