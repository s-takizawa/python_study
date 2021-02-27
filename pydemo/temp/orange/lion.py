
class Lion:
    def __init__(self, name, number=1):
        self.name = name
        self.n = number

    def __repr__(self):
        return self.name

    def __add__(self, other):
        return abs(self.n + other.n)


lion = Lion("gaoo", 10)
print(lion)

x = Lion("hoge", -20)
y = Lion("fuga", 10)
print(x + y)

tora = Lion("torao")
same_tora = tora
print(tora is same_tora)
neko = Lion("neko")
print(tora is neko)


def is_none(x):
    if x is None:
        print("x is None")
    else:
        print("x is not None")

x = 10
is_none(x)
x = None
is_none(x)
