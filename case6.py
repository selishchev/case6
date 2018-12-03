# Формула стороны шестиугольника
# num_of_hexagons - кол-во шестиугольников, которое вводит пользователь
import ru_local
import turtle
from math import sqrt

def ourcolors():
    colorsName = ('{}'.format(ru_local.RED), '{}'.format(ru_local.BLUE), '{}'.format(ru_local.GREEN), '{}'.format(ru_local.YELLOW), '{}'.format(ru_local.GRAY), '{}'.format(ru_local.PURPLE), '{}'.format(ru_local.CYAN))
    return colorsName

def listcolors():
    colorsName = ourcolors()
    colorsEng = ('\033[91m',  '\033[94m', '\033[92m', '\033[93m',  '\033[90m',  '\033[95m', '\033[96m')
    EndColor = '\033[0m'
    print('{}'.format(ru_local.LIST))
    for i in range(len(colorsName)):
        print(colorsEng[i] + colorsName[i] + EndColor)


def draw_hexagon(x, y, side_len, color):
    """Рисование шестиугольника"""
    count = 0
    turtle.goto(x, y)
    turtle.fillcolor(color)
    turtle.down()
    turtle.begin_fill()
    turtle.right(30)
    while count < 6:
        turtle.forward(side_len)
        turtle.left(60)
        count += 1
    turtle.end_fill()
    turtle.left(30)
    turtle.up()

def get_color_choice():
    colorsName = ourcolors()
    clrinput = ""
    clrexist = False
    while not clrexist:
        clrinput = input('{}'.format(ru_local.SYC)).lower()
        if clrinput in colorsName:
            clrexist = True
        else:
            print('{}'.format(ru_local.WRONG))
            clrexist = False
    return clrinput

def get_num_hexagons():
    numhex = 0
    while numhex < 4:
        try:
            numhex = int(input('{}'.format(ru_local.HEX)))
            if numhex > 20:
                numhex = 0
        except ValueError:
            numhex = 0
    return numhex

listcolors()
SelectColor1 = get_color_choice()
SelectColor2 = get_color_choice()

inputcnt = get_num_hexagons()








