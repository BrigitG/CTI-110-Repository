import turtle

t = turtle.Turtle()

wn = turtle.Screen()        
wn.bgcolor("blue")

t.color("pink")            
t.pensize(7)
t.speed(1)

count = 0
while count < 4:
    t.forward(100)
    t.right(90)
    count += 1

count = 0
while count < 3:
    t.forward(100)
    t.left(120)
    count += 1

turtle.done()

