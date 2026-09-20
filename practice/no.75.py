class circle():
    p = 3.14
    def __init__(self, r):
        self.r = r

    def masahat(self):
        m = self.r * self.r * self.p
        return m

a = int(input("r: "))
my_circle = circle(a)
masahat = my_circle.masahat()

print(masahat)