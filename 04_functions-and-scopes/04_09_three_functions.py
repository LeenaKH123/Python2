# Write a program with three functions. Each function must call
# at least one other function and use the return value
# of that function to do something with it. You can have more
# than three functions, and they don't need to call each other
# in a circular way.
# import sys
# print(sys.getrecursionlimit(1500))
def fun1(a, b):
    c = a + b
    if (a + b) > 0:
        return c
        d = fun2(6, 7)


def fun2(x, y):
    z = x * y
    if (x + y) > 0:
        return z
        f = fun3(15)


def fun3(z):
    if z > 0:
        return z
        h = fun1(3, 6) + fun2(4, 9)


print(fun1(9, 10), fun2(20, 40), fun3(10))
