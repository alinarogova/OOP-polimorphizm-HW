from math import pi
import json
print("Task 1".center(40, "="))
# Завдання 1
# Створити базовий клас Фігура з методом для підрахунку площі. Створити похідні класи: прямокутник,
# коло, прямокутний трикутник, трапеція зі своїми методами для підрахунку площі.


class Figure:
    def __init__(self, figure_type):
        self.figure_type = figure_type

    def area(self):
        return f'The area of {self.figure_type} is '


class Rectange(Figure):
    def __init__(self, a, b):
        super().__init__("rectange")
        self.a = a
        self.b = b

    def area(self):
        return super().area() + f"{self.a*self.b}."


class Cirlce(Figure):
    def __init__(self, r):
        super().__init__("cirlce")
        self.r = r

    def area(self):
        return super().area() + f"{round(2*pi*self.r, 2)}."


class RightTriangle(Figure):
    def __init__(self, a, b):
        super().__init__("right triangle")
        self.a = a
        self.b = b

    def area(self):
        return super().area() + f"{self.a * self.b / 2}."


class Trapezoid(Figure):
    def __init__(self, a, b, h):
        super().__init__("trapezoid")
        self.a = a
        self.b = b
        self.h = h

    def area(self):
        return super().area() + f"{(self.a + self.b) * self.h / 2}."


rec = Rectange(5, 4)
circle = Cirlce(5)
triangle = RightTriangle(5, 4)
trap = Trapezoid(6, 8, 10)
arr = [rec, circle, triangle, trap]
for fig in arr:
    print(fig.area())
print()

print("Task 2".center(40, "="))


class Rectange2(Figure):
    def __init__(self, a, b):
        super().__init__("rectange")
        self.a = a
        self.b = b

    def __int__(self):
        return int(self.a*self.b)

    def __str__(self):
        return (f"Figure type: {self.figure_type}\n"
                f"Sides: {self.a}, {self.b}")


class Cirlce2(Figure):
    def __init__(self, r):
        super().__init__("cirlce")
        self.r = r

    def __int__(self):
        return int(2*pi*self.r)

    def __str__(self):
        return (f"Figure type: {self.figure_type}\n"
                f"Radius: {self.r}")


class RightTriangle2(Figure):
    def __init__(self, a, b):
        super().__init__("right triangle")
        self.a = a
        self.b = b

    def __int__(self):
        return int(self.a * self.b / 2)

    def __str__(self):
        return (f"Figure type: {self.figure_type}\n"
                f"Sides: {self.a}, {self.b}")


class Trapezoid2(Figure):
    def __init__(self, a, b, h):
        super().__init__("trapezoid")
        self.a = a
        self.b = b
        self.h = h

    def __int__(self):
        return int((self.a + self.b) * self.h / 2)

    def __str__(self):
        return (f"Figure type: {self.figure_type}\n"
                f"Sides: {self.a}, {self.b}\n"
                f"Height: {self.h}")


rec = Rectange2(5, 4)
circle = Cirlce2(5)
triangle = RightTriangle2(5, 4)
trap = Trapezoid2(6, 8, 10)
arr = [rec, circle, triangle, trap]

for fig in arr:
    print(fig)
    print("Area:", int(fig), "\n")

print("Task 3".center(60, "="))
'''
Завдання 3
Створіть базовий клас Shape для малювання плоских фігур.
Визначте методи:
■ Show() - виведення на екран інформації про фігуру;
■ Save() - збереження фігури у файл;
■ Load() - зчитування фігури з файлу.
'''


class Shape:
    def __init__(self, shape_type):
        self.shape_type = shape_type

    def show(self):
        return f"{self.shape_type}: "

    @classmethod
    def load(cls, filename: str):
        """
        Завантаження фігур з файлу
        """
        figures = []
        with open(filename, 'r') as f:
            for line in f:
                data = json.loads(line.strip())
                if data['shape_type'] == 'Square':
                    figures.append(Square(data['x'], data['y'], data['a']))
                elif data['shape_type'] == 'Rectangle':
                    figures.append(Rectangle(data['x'], data['y'], data['a'], data['b']))
                elif data['shape_type'] == 'Circle':
                    figures.append(Circle(data['x'], data['y'], data['r']))
                elif data['shape_type'] == 'Ellipse':
                    figures.append(Ellipse(data['x'], data['y'], data['a'], data['b']))
        return figures

    @staticmethod
    def save(file_name, to_json):
        with open(file_name, 'a') as f:
            f.write(json.dumps(to_json)+"\n")

    @staticmethod
    def clear(file_name):
        with open(file_name, 'w') as f:
            f.write("")


'''
Визначте похідні класи:
■ Square - квадрат, який характеризується координатами лівого верхнього кута та довжиною сторони;
■ Rectangle - прямокутник із заданими координатами верхнього лівого кута та розмірами;
■ Circle - коло із заданими координатами центру і радіусом;
■ Ellipse - еліпс із заданими координатами верхнього кута описаного навколо нього прямокутника зі сторонами,
паралельними осям координат, і розмірами цього прямокутника.
Створіть список фігур, збережіть фігури у файл, завантажте в інший список і відобразіть інформацію про кожну з фігур
'''


class Square(Shape):
    def __init__(self, x, y, a):
        super().__init__("Square")
        self.x = x
        self.y = y
        self.a = a

    def show(self):
        return super().show() + f"\n  Coordinate: ({self.x}, {self.y})" + f"\n  Side lenght: {self.a}"


class Rectangle(Shape):
    def __init__(self, x, y, a, b):
        super().__init__("Rectangle")
        self.x = x
        self.y = y
        self.a = a
        self.b = b

    def show(self):
        return super().show() + f"\n  Coordinate: ({self.x}, {self.y})" + f"\n  Sides lenght: {self.a}, {self.b}"


class Circle(Shape):
    def __init__(self, x, y, r):
        super().__init__("Circle")
        self.x = x
        self.y = y
        self.r = r

    def show(self):
        return super().show() + f"\n  Coordinate: ({self.x}, {self.y})" + f"\n  Radius: {self.r}"


class Ellipse(Shape):
    def __init__(self, x, y, a, b):
        super().__init__("Ellipse")
        self.x = x
        self.y = y
        self.a = a
        self.b = b

    def show(self):
        return super().show() + f"\n  Coordinate: ({self.x}, {self.y})" + f"\n  Sides lenght: {self.a}, {self.b}"


file_name = "data.txt"
square = Square(1, -1, 4)
rectangle = Rectangle(0, 1, 2, 3)
circle = Circle(0, 0, 1)
ellipse = Ellipse(-3, -2, 4, 5)

shapes = [square, rectangle, circle, ellipse]
for shape in shapes:
    print(shape.show())
    print()

#circle.clear(file_name)
shapes2 = Shape.load(file_name)
for shape in shapes2:
    print(shape.show())
    print()
