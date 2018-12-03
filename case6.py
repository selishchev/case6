"""Case-study #5 Tesselation
Developers:
Selishchev A. 35%, Paymushkin K.35%, Krivosheenkova E.30%"""

from turtle import *
from math import *
import ru_local
def draw_hexagon(x, y, side_len, color):
    """Drawing a hexagon"""
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
    num_of_hexagons=int(input('{}'.format(ru_local.HEX)))
    if 3 < num_of_hexagons < 21:
        return num_of_hexagons
    else:
        return get_num_hexagons()

def draw(color1, color2, count):
    """Drawing all hexagons"""
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
    list_of_colors = ['{}'.format(ru_local.RED), '{}'.format(ru_local.BLUE),
                      '{}'.format(ru_local.GREEN), '{}'.format(ru_local.YELLOW),
                      '{}'.format(ru_local.ORANGE), '{}'.format(ru_local.PURPLE),
                      '{}'.format(ru_local.PINK)]
    print('{}'.format(ru_local.LIST))
    for c in list_of_colors:
        print('', c)
    colors_codes = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink']
    color = str(input('{}'.format(ru_local.SYC)))
    color_re = color.lower()
    color_rem = color_re.replace('{}'.format(ru_local.YO), '{}'.format(ru_local.YE))
    for i in range(len(colors_codes)):
        if color_rem == list_of_colors[i]:
            return colors_codes[i]
    while True:
        color = str(input('{} {}'.format(color,'{}'.format(ru_local.WRONG))))
        for i in range(len(colors_codes)):
            if color_rem == list_of_colors[i]:
                return colors_codes[i]

def main():
    count = get_num_hexagons()
    color_1 = get_color_choice()
    color_2 = get_color_choice()
    screensize(500, 500)
    draw(color_1, color_2, count)


if __name__ == '__main__':
    main()