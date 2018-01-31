word = input("Input a word: ")
world_list = list(word)
print(world_list)

result = []
for _ in range(len(world_list)):
    result.append(world_list.pop())
print(result)
print(word[::-1])
