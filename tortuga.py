import turtle
window = turtle.Screen()
tortuga = turtle.Turtle()

"""

tortuga.forward(100)
tortuga.right(120)
turtle.fillcolor("red")
tortuga.forward(100)
tortuga.right(60)

tortuga.forward(100)
tortuga.right(120)

tortuga.forward(100)


window.mainloop()
"""
turtle.fillcolor("red")
turtle.begin_fill()
for i in range(4):
    turtle.forward(100)
    turtle.right(90)
turtle.end_fill()
