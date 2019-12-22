import math
import cmath
from random import randint
import timeit

#1
def dictionary():
    d = {}

    for i in range(44, 90, 5):
        y = i * i + 1
        d[i] = str(i) + str(" * ") + str(i) + " + 1 = " + str(y)
        print(d[i])

dictionary()

#2

fib_lambda = lambda n: fib_lambda(n - 1) + fib_lambda(n - 2) if n > 2 else 1

def fib(n):
    a = 0
    b = 1

    for __ in range(n):
        a, b = b, a + b

    return a

n = randint(10, 26)

def fibonacci():
    print("\n")
    print(str(n) + "-ое число Фиббоначчи = " + str(fib(n)))
    print("fib отработало за " + str(timeit.timeit('fib(n)', 'from __main__ import fib, n')))
    print("fib_lambda отработало за " + str(timeit.timeit('fib_lambda(n)', 'from __main__ import fib_lambda, n')))

fibonacci()

#3

def my_cos(x, n = 30):

    q = 1
    s = 0

    for i in range(1, n + 1):
        s = s + q
        q = q * (-1) * (x * x) / ((2 * i - 1) * (2 * i))

    return s


def my_sin(x, n = 30):

    q = x
    s = 0

    for i in range(1, n + 1):
        s = s + q
        q = q * (-1) * (x * x) / ((2 * i + 1) * (2 * i))

    return s

def my_ln(x, n = 30):
    x -= 1
    s = 0

    for i in range(1, n + 1):
        s += ((-1) ** (i+1) * (x ** i)) / i

    return s

def my_exp(x, n = 30):
    s = 0

    for i in range(n):
        s += x ** i / math.factorial(i)

    return s

def teylor():
    mc = my_cos(math.radians(60))
    ms = my_sin(math.radians(45))
    mln = my_ln(0.5)
    mex = my_exp(0.2)
    print("my_cos(60): " + str(mc))
    print("my_sin(45): " + str(ms))
    print("my_ln(0.5): " + str(mln))
    print("my_exp(0.2): " + str(mex))

    cx = complex(2, 3)
    mc = my_cos(cmath.phase(cx))
    print("my_cos from complex number", cx, ": ", mc)

teylor()