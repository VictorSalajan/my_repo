import pylab as plt

def fib(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def gatherFibs(n):
    inputs = list(range(n))
    results = []
    for i in range(n):
        results.append(fib(i))
    return inputs, results

def displayFibs(n):
    (xvals, yvals) = gatherFibs(n)
    plt.figure('fibs')
    plt.plot(xvals, yvals, label = 'fibonacci')
    plt.title('Fibonacci sequence')
    return (xvals, yvals)


print(displayFibs(20))
plt.show()
