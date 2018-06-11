
def fib(n):
    if n == 1 or n == 2:
        return 1
    fib_array = [None] * (n + 1)
    fib_array[1] = 1
    fib_array[2] = 1
    for i in range(3,n + 1):
        fib_array[i] = fib_array[i - 1] + fib_array[i - 2]
    return fib_array[n]

if __name__ == '__main__':
    print(fib(100))