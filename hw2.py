import collections

#1

def even_nums(a = 1000, b = 5000):
    for j in range(a, b + 1):
        i = j
        while (i != 0) & ((i % 10) % 2 == 0):
            i = i // 10
        if i == 0:
            print(j)

even_nums()

#2

def current_row(k):
    row = list()
    for i in range(k):
        if i == 0 or i == k - 1:
            row.append(1)
        else:
            c_row = current_row(k - 1)
            row.append(c_row[i - 1] + c_row[i])
    return row

def pascal_triangle(n, step = 1):
    result = list()
    for i in range(n):
        result.append(current_row(i + 1))
    for j in range(0, n, step):
        print(result[j])

pascal_triangle(10, 2)


#3

def multiargs(*args):
    c = collections.Counter()
    for v in args:
        c[type(v)] += 1
    print(dict(c))

multiargs("One", "Sinus", 1, 2, 3, 44, 0, 1/2, 3.0, 5.6)