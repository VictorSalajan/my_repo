import time

def fib(n):
    global numFibCalls
    numFibCalls += 1

    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def fastFib(n, memo = {}):
    """Assumes n is an int >= 0, memo used only by recursive calls
       Returns Fibonacci of n"""
    global numFibCalls
    numFibCalls += 1

    if n == 0 or n == 1:
        return 1
    try:
        return memo[n]
    except KeyError:
        result = fastFib(n-1) + fastFib(n-2)
        memo[n] = result
        return result

numFibCalls = 0
start = time.time()

for i in range(32):
    print(f'fib({str(i)}) = {fib(i)}')

delta_time = time.time() - start
fib_info = f'It took {round(delta_time, 4)} seconds and {numFibCalls} function calls to run fib(35)'


numFibCalls = 0
start = time.time()

for i in range(32):
    print(f'fastFib({str(i)}) = {fastFib(i)}')

delta_time = time.time() - start


print(fib_info)
print(f'It took {round(delta_time, 4)} seconds and {numFibCalls} function calls to run fib_dynamic(35)')
