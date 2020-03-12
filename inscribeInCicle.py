from turtle import Turtle, mainloop, tracer, update
import math

r = 200
sides = 9
th = 0
n = 0
t = Turtle()
tracer(0)
#t.penup()
#t.setpos(r*math.cos(th), r*math.sin(th))
#t.pendown()
#t.right(45)
#t.fd(100)
#t.left(90)
#ocotagon
'''
t.left(45+22.5)
t.fd(100)
t.left(90+22.5)
t.fd(100)
t.left(90+22.5)
t.fd(100)
'''

'''
t.setpos(-45,100)
for n in range(8):
  t.fd(100)
  t.right(45)
'''

update()
'''
t.fd(100)
t.right(90+22.5)
t.fd(100)
t.right(90+22.5)
t.fd(100)
'''

#circle
t.penup()
t.setpos(r*math.cos(th), r*math.sin(th))
t.pendown()  
while th <= 2*math.pi:
  th += math.pi/100
  t.setpos(r*math.cos(th), r*math.sin(th))

update()

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
 
  





  

