from turtle import Turtle, mainloop, tracer, update
import math

r = 200
sides = 8

t = Turtle()
tracer(0)

#circle
th = 0
t.penup()
t.setpos(r*math.cos(th), r*math.sin(th))
t.pendown()  
while th <= 2*math.pi:
  th += math.pi/100
  t.setpos(r*math.cos(th), r*math.sin(th))

update()

#polygon
t.penup()
angle = (2*math.pi)/(2*sides)
y = r*math.sin(angle)
x = r*math.cos(angle)
t.setpos(x, -y)
t.left(90)
t.pendown()
for n in range(sides):
  t.fd(2*y)
  t.left(360/sides)

update()








  

