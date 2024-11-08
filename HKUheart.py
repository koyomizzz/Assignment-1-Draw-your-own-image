import turtle

screen = turtle.Screen()
t = turtle.Turtle()
t.color('red') 

t.begin_fill()

# 画爱心
t.fillcolor('red')  
t.left(140)
t.forward(224)
for _ in range(200):
    t.right(1)
    t.forward(2)

t.left(120)
for _ in range(200):
    t.right(1)
    t.forward(2)

t.end_fill()


# 写上 "HKU"
t.penup()
t.color('black') 
t.goto(-50, -100)  
t.write("HKU", font=("Arial", 50, "normal"))


t.hideturtle()
screen.mainloop()