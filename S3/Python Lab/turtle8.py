import turtle
def draw_petal(t,radius,angle):
    for _ in range(2):
        t.circle(radius,angle)
        t.left(180-angle)
def draw_flower(petals,radius=100,angle=60):
    wn=turtle.Screen()
    wn.bgcolor("white")
    t = turtle.Turtle()
    t.color("red")
    t.speed(0)
    for _ in range(petals):
        draw_petal(t,radius,angle)
        t.left(360/petals)
    t.hideturtle()
    wn.mainloop()
draw_flower(petals=12)