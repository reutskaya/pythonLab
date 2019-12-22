from random import uniform, randint
from functools import reduce


#1

def last_10_days_temperature():
    temperatures = list()
    for i in range(10):
        temperatures.append(uniform(10, 25))
    print("Celsius start values:", temperatures)
    ftemperatures = list(map(lambda x: 9 / 5 * x + 32, temperatures))
    print("Fahrenheit:", ftemperatures)
    ctemperatures = list(map(lambda x: 5 / 9 * (x - 32) + 273.15, ftemperatures))
    print("Calvin:", ctemperatures)
    temperatures1 = list(map(lambda x: x - 273.15, ctemperatures))
    print("Celsius finish values:", temperatures1)
    print("Differeces:", list(map(lambda x, y: abs(x - y), temperatures1, temperatures)))

last_10_days_temperature()

#2

def dict_filter(d):
    return dict(filter(lambda x: type(x[0]) == type(""), d.items()))

def dictionaries_merge():
    d = {'x':2, 4:'y', 4.0:'12', '3':'fdfs', 'a':9., b'pp':52}
    print("\n")
    print(dict_filter(d))

dictionaries_merge()

#3

def list_prod(a,b):
    return reduce(lambda x, y: x * y, list(map(lambda t: t[0] + t[1], list(zip(a, b[::-1])))))

def multiply_arrays():
    n = randint(4,8)
    a, b = list(), list()
    for __ in range(n):
        a.append(randint(1,10))
        b.append(randint(1,10))
    print("\n")
    print(list_prod(a, b))

multiply_arrays()