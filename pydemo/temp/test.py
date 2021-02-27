import math
import random



print("start")


def f(x):
    return x*2


ret = f(20)
print(ret)


def even_odd(x=2):
    if x % 2 == 0:
        print("gusu")
    else:
        print("kisu")


even_odd(5)
even_odd()

try:
    print(10 / 0)
except ZeroDivisionError:
    print("zero div")


def add(x, y):
    """
    hoge
    :param x: int.
    :param y: int.
    """
    return x + y


print(add(10, 20))
print("hoge".upper())


fruit = ["apple", "grapes"]
fruit.append("banana")
print(fruit)
print(len(fruit))

my_tuple = ("1", True, "abc")

print(my_tuple[1])

my_dict = {"a": 1, "b": "banaan"}
print(my_dict["b"])


print(math.pow(2, 3))
print(random.randint(0, 100))

print("""end""")
