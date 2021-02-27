
class Orange:
    def __init__(self, w, c):
        self.weight = w
        self.color = c
        self.mold = 0
        print("Createed")

    def rot(self, days, temp):
        """tempareture"""
        self.mold = days * temp


# orange = Orange(10, "dark")

# print(orange.mold)

# orange.rot(3, 6)


# print(orange.mold)
