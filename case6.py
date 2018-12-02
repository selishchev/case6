"""Case-study #5 Tesselation
Developers:
Selishchev A., Paymushkin K., Krivosheenkova E.

"""
import turtle
from math import sqrt


def draw_hexagon(x, y, side_len, color):
    """Рисование шестиугольника"""
    count = 0
    turtle.goto(x, y)
    turtle.fillcolor(color)
    turtle.down()
    turtle.beginfill()
    turtle.right(30)
    while count < 6:
        turtle.forward(side_len)
        turtle.left(60)
        count += 1
    turtle.endfill()
    turtle.left(30)


# Формула стороны шестиугольника
# num_of_hexagons - кол-во шестиугольников, которое вводит пользователь
side_len = float(sqrt(4 * (500 / (2 * num_of_hexagons)) ** 2 / 3))
