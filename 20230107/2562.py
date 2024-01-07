n = []
for i in range(9):
    a = int(input())
    n.append(a)

max_value = max(n)
max_index = n.index(max_value)

print(max_value)
print(max_index + 1)
