import turtle

def draw_square(some_turtle):
    for iterations in range(4):
        some_turtle.forward(100)
        some_turtle.left(90)

def draw_cirlewithsquares():
    window = turtle.Screen()
    window.bgcolor("red")
    brad = turtle.Turtle()
    brad.speed(10)

    for i in range(37):
        draw_square(brad)
        brad.right(10)

    window.exitonclick()

draw_cirlewithsquares()
