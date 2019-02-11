from turtle import *


boogie = Turtle()

boogie.color("pink")
boogie.pensize(5)
boogie.speed(8)
boogie.turtlesize(4,4,4)
boogie.shape("turtle")



for x in range(7):
	boogie.forward(80)
	boogie.left(70)



mainloop()
