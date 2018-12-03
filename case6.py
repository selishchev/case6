from turtle import *
from math import *
def draw_hexagon(x, y, side_len, color):
    """Рисование шестиугольника"""
    count = 0
    goto(x, y)
    fillcolor(color)
    down()
    begin_fill()
    right(30)
    while count < 6:
        forward(side_len)
        left(60)
        count += 1
    end_fill()
    left(30)
    up()
def get_num_hexagons():
    num_of_hexagons=int(input('введите кол-во'))
    if 3 < num_of_hexagons < 21:
        return num_of_hexagons

def draw(color1, color2, count):
    """Рисование всех шестиугольников"""
    side_len = float(sqrt(4 * (500 / (2 * count)) ** 2 / 3))
    speed(0)
    y = 250
    x = -250
    line = 1
    for lines in range(count):
        up()
        for hexagons in range(count):
            fillcol = color1
            draw_hexagon(x, y, side_len, fillcol)
            x = xcor() + sqrt(side_len ** 2 - (side_len / 2) ** 2) * 2
            color1, color2 = color2, color1
        if count % 2:
            color1, color2 = color2, color1
        if line % 2:
            j = 1
        else:
            color1, color2 = color2, color1
            j = 3
        y = ycor() - 3 * side_len / 2
        x = xcor() - (count * 2 - j) * sqrt(side_len ** 2 - (side_len / 2) ** 2)
        goto(x, y)
        line += 1
    done()

def get_color_choice():
    list_of_colors = ['красный', 'синий', 'зеленый', 'желтый', 'оранжевый', 'пурпурный', 'розовый']
    print('допустимые цвета заливки:')
    for c in list_of_colors:
        print('', c)
    colors_codes = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink']
    color = str(input('введите цвет йоу:')).lower()
    for i in range(7):
        if color == list_of_colors[i]:
            return colors_codes[i]
def main():
    count = get_num_hexagons()
    color_1 = get_color_choice()
    color_2 = get_color_choice()
    screensize(500, 500)
    draw(color_1, color_2, count)

main()
