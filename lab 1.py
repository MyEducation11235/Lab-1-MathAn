import turtle
import random
from math import *

def sign(n):
    return 1 if n >= 0 else -1

def myRound(f, n = 0):
    return int(f * 10**n + 0.5 * sign(f)) / 10**n

def readInputData():
    global divisions
    global getIndexRectHeight
    divisions = int(input("Введите число точек разбиения\n"))
    
    global rectWidth
    rectWidth = (finX - startX) / divisions # ширина однго раздиения

    while True:
        c = input("Выберите способ выбора оснащения:\n\tL - левые\n\tM - средние\n\tR - правые\n\tA - случайные\n")
        match c:
            case 'l' | 'L':
                getIndexRectHeight = lambda : 0
                break
            case 'm' | 'M':
                getIndexRectHeight = lambda : int(rectWidth * zoom) // 2
                break
            case 'r' | 'R':
                getIndexRectHeight = lambda : int(rectWidth * zoom) - 1
                break
            case 'a' | 'A':
                getIndexRectHeight = lambda : random.randint(0, int(rectWidth * zoom) - 1)
                break
            case _:
                print("Не найденно соответствие!\n==============\n")

def F(x):                   # наша прекрасная функция
    return sin(x)       # вар 11
    #return e**-x       # вар 16
    #return cos(2 * x)  # вар 28

singleSegmentX = pi / 4          # еденичный отрезок по X
singleSegmentY = 0.2          # еденичный отрезок по Y
startX = 0                  # начало ООФ
finX = 2 * pi               # конец ООФ вар 11
#finX = 2                    # конец ООФ вар 16
#finX = pi                   # конец ООФ вар 28
startY = -1                 # начало ОДЗ
finY = 1                    # конец ОДЗ

zoom = 175                  # увеличить изобраение в zoom раз
cordOriginX = -600          # сместить график в окне по X
cordOriginY = 0             # сместить график в окне по Y
colorChart = "#7f00ff"      # цвет графика
colorRect = "#ff0000"       # цвет прямоугольничков
colorStopLine = "#ffff00"   # цвет линий ограничивающий ООФ



def teleport(T, x, y):
    T.pu()
    T.goto(cordOriginX + x, cordOriginY + y)
    T.pd()

def drawAxes(x_lt, y_lt, x_rb, y_rb, x_step = 1, y_step = 1):

    def drawAxe(T, length, step, fromNumber, shift):
        T.fd(-step // 2)
        T.fd(step // 2)
        for i in range(0, length // step + 1):
            T.dot()
            if(abs(fromNumber + i * step / zoom) > 0.01):
                T.pu()
                T.left(90)
                T.fd(shift)
                T.pd()
                T.write(myRound(fromNumber + i * step / zoom, 2))
                T.pu()
                T.fd(-shift)
                T.right(90)
                T.pd()
            if(i == length // step):
                T.fd(step // 2)
            else:
                T.fd(step)
                
    X = turtle.Turtle()
    X.speed(0)
    X.pensize(2)
    teleport(X, x_lt, 0)
    drawAxe(X, x_rb - x_lt, x_step, startX, -20)
    X.write("x")
    
    Y = turtle.Turtle()
    Y.speed(0)
    Y.pensize(2)
    teleport(Y, 0, y_rb)
    Y.left(90)
    drawAxe(Y, y_lt - y_rb, y_step, startY, 20)
    Y.write("y")

def drawRect(x_lt, y_lt, x_rb, y_rb):
    T = turtle.Turtle()
    T.hideturtle()
    T.speed(0)
    T.color("#ff0000")
    teleport(T, x_lt, y_lt)
    for i in range(2):
        T.forward(x_rb - x_lt)
        T.right(90)
        T.forward(y_lt - y_rb)
        T.right(90)


readInputData()


drawAxes(int(startX * zoom), int(finY * zoom), int(finX * zoom), int(startY * zoom), int(singleSegmentX * zoom), int(singleSegmentY * zoom))

T = turtle.Turtle()
T.speed(0)
T.hideturtle()

T.color(colorStopLine)
teleport(T, startX * zoom, startY * zoom - zoom / 2)
T.goto(startX * zoom + cordOriginX, finY * zoom + cordOriginY + zoom / 2)
teleport(T, finX * zoom, startY * zoom - zoom / 2)
T.goto(finX * zoom + cordOriginX, finY * zoom + cordOriginY + zoom / 2)

T.color(colorChart)
T.pensize(2)
teleport(T, startX * zoom, F(startX) * zoom)

integralSum = 0.0

rectHeight = 0
for n in range(0, divisions):
    indexRectHeight = getIndexRectHeight()
    rectStart = startX + rectWidth * n
    for i in range(0, int((rectWidth) * zoom)):    
        x = rectStart + i / zoom
        f = F(x)
        T.goto(x  * zoom + cordOriginX, f * zoom + cordOriginY)
        if(i == indexRectHeight):
            rectHeight = f
            T.color(colorRect)
            T.dot()
            T.color(colorChart)
            drawRect(rectStart * zoom, rectHeight * zoom, (rectStart + rectWidth) * zoom, 0)
            integralSum += rectHeight * rectWidth
    
teleport(T, (startX + finX) / 2 * zoom, finY * zoom + 40)
T.write("Интегральная сумма = " + str(myRound(integralSum, 7)))
teleport(T, (startX + finX) / 2 * zoom, finY * zoom + 55)
T.write("Число разбиений = " + str(divisions))

print("\nИнтегральная сумма =", myRound(integralSum, 7), "\n")

turtle.exitonclick()
#turtle.Screen().mainloop()

