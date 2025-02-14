import turtle

screen=turtle.Screen()
screen.setup(800,800)

t=turtle.Turtle()
t.color("yellow")
t.speed(0)

t.up()
t.goto(0,-200)
t.down()
t.begin_fill()
t.circle(200)
t.end_fill()

t.up()
t.goto(-75,50)
t.down()
t.color("black")
t.begin_fill()
t.circle(35)
t.end_fill()

t.up()
t.goto(75,50)
t.down()
t.begin_fill()
t.circle(35)
t.end_fill()

t.up()
t.goto(114,-20)
t.down()
t.width(10)
t.right(109)
for y in range (5):
    t.forward(70)
    t.right(36)

turtle.done()
