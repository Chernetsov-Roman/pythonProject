class Shape:
    """класс фигура"""

    def Square(self):
        print("Данный метод не определен для текущего класса")

class Circle(Shape):
    """Класс круг"""

    name = 'circle'

    def __init__(self, radius, x, y):
        self.radius = radius
        self.x = x
        self.y = y

    def Square(self):
        s = 3.14 * self.radius**2
        print(f'Площадь окружности c радиусом = {self.radius} = {s}')

    def ShowCentr(self):
        print(f'Центр х = {self.x}, у = {self.y}')

class Ractangle(Shape):
    name = "Ractangle"
    def __init__(self, h, w):
        self.h = h
        self.w = w

    def Square(self):
        print(f'Площадь прямоугольника со торонами'
              f' А = {self.h}, В = {self.w} '
              f'равна', self.h * self.w)

c = Ractangle(10, 20)
c.Square()


# a = Circle(10, 2, 4)
# a.Square()
#
# a.ShowCentr()


