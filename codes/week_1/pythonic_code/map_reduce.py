# Map

def f(x, y):
    return x + y
f(1, 4)


f = lambda x,y: x+y
f(1, 4)


ex = [1, 2, 3, 4, 5]
f = lambda x: x ** 2
print(list(map(f, ex)))


ex = [1, 2, 3, 4, 5]
f = lambda x, y: x + y
print(list(map(f, ex, ex)))

list(map(
    lambda x: x ** 2 if x % 2 == 0 else x,
    ex))

#python 3에는 list를 꼭 붙여줘야함
ex = [1,2,3,4,5]
print(list(map(lambda x: x+x, ex)))
print((map(lambda x: x+x, ex)))

f = lambda x: x ** 2
print(map(f, ex))
for i in map(f, ex):
    print(i)

result = map(f, ex)
print(result)
print(next(result))

import sys
sys.getsizeof(ex)
sys.getsizeof((map(lambda x: x+x, ex)))
sys.getsizeof(list(map(lambda x: x+x, ex)))

# Reduce
from functools import reduce
print(reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))


def factorial(n):
    return reduce(
            lambda x, y: x*y, range(1, n+1))


factorial(5)
