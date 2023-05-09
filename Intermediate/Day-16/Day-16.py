# from turtle import Turtle, Screen
#
# timmy = Turtle() # This is an object created
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)
# timmy.left(45)
# timmy.forward(200)
# timmy.right(90)
# timmy.forward(150)
# my_screen = Screen()
#
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander", "ditmemay"])
table.add_column("Type", ["Electric", "Water", "Fire", "vailon"])
table.align = "l"
print(table)

