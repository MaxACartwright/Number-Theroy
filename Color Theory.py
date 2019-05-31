import turtle as t

t.speed(1000)

data = [[10, 10], [255, 255]]

t.forward(256)
t.left(90)
t.forward(256)
t.left(90)
t.forward(256)
t.left(90)
t.forward(256)

for i in range(len(data)):
    t.penup()
    t.goto(data[i][0],data[i][1])
    t.pendown()
    t.circle(2)

