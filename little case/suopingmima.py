"""
作者：Lucky
功能：锁屏
"""
import turtle
def circle():

    i=-100
    for x in range(3):
        turtle.penup()
        turtle.goto(0, -(i+100))
        turtle.pendown()
        turtle.circle(3, 360)
        for y in range(2):
            turtle.penup()
            turtle.forward(100)
            turtle.pendown()
            turtle.circle(3, 360)
        i+=100

def main():
    circle()
    turtle.penup()
    turtle.goto(100,-100)
    turtle.pendown()
    turtle.pencolor("blue")
    turtle.pensize(10)
    turtle.left(90)
    turtle.forward(100)
    turtle.right(153.435)
    count = 1
    while count <= 4:
        count = count+1
        turtle.forward(223.606)
        turtle.right(143.13)
        turtle.forward(223.606)
        turtle.right(126.87)

    turtle.exitonclick()
if __name__ == '__main__':
    main()
