from functools import reduce

fib_series = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]], range(n - 2), [0, 1])

result = fib_series(50)
print(result)