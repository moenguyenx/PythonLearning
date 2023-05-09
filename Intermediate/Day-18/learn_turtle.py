import turtle as t
import random


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


tim = t.Turtle()
tim.shape("arrow")
tim.pensize(5)
tim.speed(0)

t.colormode(255)
for i in range(200):
    t.color(random_color())
    t.circle(100)
    t.right(10)

# TODO: Draw a spirograph
def draw_spirograph(size_of_gap):
    for i in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(10)



# TODO: Generate a random walk and random RGB colors


# direction = [0, 90, 180, 270]
# for _ in range(100):
#     tim.color(random_color())
#     tim.forward(40)
#     tim.setheading(random.choice(direction))

# TODO: Drawing different shapes
# for _ in range(10):
#     tim.pendown()
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#
# tim.pendown()
# def draw(sides):
#     angle = 360 / sides
#     for _ in range(sides):
#         tim.forward(100)
#         tim.right(angle)
#
#
# for num_sides in range(3, 11):
#     tim.color(random.choice(colours))
#     draw(num_sides)

screen = t.Screen()
screen.exitonclick()
