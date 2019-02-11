from turtle import *


boogie = Turtle()
noel = Turtle() 

boogie.color("turquoise")
boogie.pensize(8)
boogie.speed(3)
boogie.turtlesize(4,4,4)
boogie.shape("turtle")

noel.color("red")
noel.pensize(8)
noel.speed(3)
noel.turtlesize(4,4,4)
noel.shape("turtle")



for x in range(3):
	boogie.forward(80)
	boogie.left(120)
	noel.circle(50)

mainloop()
