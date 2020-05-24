def fib_bottom_up(n):
    if n == 1 or n == 2:
        return 1
    arr = [None] * (n + 1)
    arr[1] = arr[2] = 1
    for i in range(3, n + 1):
        arr[i] = arr[i - 1] + arr[i - 2]
    return arr[n]

print(fib_bottom_up(10))
print(fib_bottom_up(100))
print(fib_bottom_up(1000))
print(fib_bottom_up(10000))
print(fib_bottom_up(100000))
