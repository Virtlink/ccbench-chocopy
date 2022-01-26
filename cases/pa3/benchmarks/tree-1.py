# Binary-search trees


# Crunch
t = Tree()
while i < n:
	t.insert(k)
	k = (k * 37813) % 37831
	if i % c != 0:
		t.insert(i)
	i = i + 1

print(t.size)

for i in [4, 8, 15, 16, 23, 42]:
	if t.contains(i):
		print(i)
