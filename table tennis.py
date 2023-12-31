import turtle
import winsound

a=0
b=0

wn=turtle.Screen()
wn.title("monik's first game")
wn.bgcolor("black")
wn.setup(width=800 , height=600)
wn.tracer(0)


b=turtle.Turtle()
b.goto(-360,0)
b.speed(0)
b.penup()
b.shape("square")
b.color("white")
b.shapesize(6,1)



d=turtle.Turtle()
d.goto(360,0)
d.speed(0)
d.penup()
d.shape("square")
d.color("white")
d.shapesize(6,1)



m=turtle.Turtle()
m.goto(0,0)
m.penup()
m.shape("square")
m.color("white")


def b_up():
    y=b.ycor()
    y=y+20
    if y!=260:
        b.sety(y)
    
def b_down():
    y=b.ycor()
    y=y-20
    if y!=-260:
        b.sety(y)    
    


def d_up():
    y=d.ycor()
    y=y+20
    if y!=260:
        d.sety(y)
    
def d_down():
    y=d.ycor()
    y=y-20
    if y!=-260:
        d.sety(y)
    
m.dx=0.15
m.dy=0.15 


wn.listen()
wn.onkeypress(b_up,"w")
wn.onkeypress(b_down,"s")
wn.listen()
wn.onkeypress(d_down,"2")
wn.onkeypress(d_up,"8")




pen=turtle.Turtle()
pen.color("white")
pen.penup()

pen.goto(0,260)
pen.hideturtle()

pen.write("Player A : 0  Player B : 0  ",align="center",font=("courier",24,"bold") )




score_a=0
score_b=0
while True:
    
    wn.update()
    if m.ycor()<b.ycor()+60  and  m.ycor()>b.ycor()-60 and m.xcor()>-370 and  m.xcor() <-359.5:
        m.setx(-340)
        m.dx=m.dx*(-1)
        winsound.PlaySound("Grenade+1.mp3",winsound.SND_ASYNC)
    if m.ycor()<d.ycor()+60 and m.ycor()>d.ycor()-60 and m.xcor()<370 and m.xcor() >359.5:
        m.setx(350)
        m.dx=m.dx*(-1)
        winsound.PlaySound("Grenade+1.mp3",winsound.SND_ASYNC)
        
    if m.xcor()>390:
        m.goto(0,0)
        m.dx=-0.15
        score_a=score_a+1
        
        pen.clear()
      
       
        pen.write("Player A : {}  Player B : {}  ".format(score_a,score_b),align="center",font=("courier",24,"bold") )
       
    if m.xcor()<-390:
        m.goto(0,0)
        m.dx=0.15
        score_b=score_b+1
        
        pen.clear()
        
        pen.write("Player A : {}  Player B : {}  ".format(score_a,score_b),align="center",font=("courier",24,"bold") )
        
    m.setx(m.xcor()+m.dx)


    if m.ycor()>290:
        m.dy=-0.15
        winsound.PlaySound("Grenade+1.mp3",winsound.SND_ASYNC)
    if m.ycor()<-290:
        m.dy=0.15
        winsound.PlaySound("Grenade+1.mp3",winsound.SND_ASYNC)
    
    m.sety(m.ycor()+m.dy)



