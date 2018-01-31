u = [2, 2]
v = [2, 3]
z = [3, 5]

result = [t for t in zip(u, v, z)]
print (result)


u = [1, 2, 3]
v = [4, 4, 4]
alpha = 2
result = [2*sum(t) for t in zip(u, v)]
print(result)
