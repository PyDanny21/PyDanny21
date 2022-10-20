import random
import turtle
import time

pen2=turtle.Turtle()
pen2.color('black')
p=pen2.getscreen().bgcolor('white')
pen2.up()
pen2.goto(0,0)
pen2.down()
pen2.showturtle()
pen2.write('WELCOME TO PYPONG GAME\n\n\nHow to play',align='center',font=('Times New Roman',22,'bold'))
pen2.up()
pen2.goto(0,-70)
pen2.down()
pen2.showturtle()
pen2.write('USE Q,A for left control and O,L for right',align='center',font=('Arial',16,'normal'))
pen2.hideturtle()
time.sleep(2)
pen2.clear()
if time.sleep(3):
    exit()

wn=turtle.Screen()
wn.title('PONG GAME')
wn.bgcolor('white')
wn.tracer(0)
wn.setup(800,600)

paddle_a=turtle.Turtle()
paddle_a.shape('square')
paddle_a.color('green')
paddle_a.speed(0)
paddle_a.shapesize(stretch_len=1,stretch_wid=5)
paddle_a.up()
paddle_a.goto(-370,0)
paddle_a.down()
paddle_a.showturtle()


paddle_b=turtle.Turtle()
paddle_b.shape('square')
paddle_b.color('green')
paddle_b.shapesize(stretch_len=1,stretch_wid=5)
paddle_b.speed(0)
paddle_b.up()
paddle_b.goto(370,0)
paddle_b.down()
paddle_b.showturtle()

ball_colors=['red','magenta','blue','violet','cyan','black','orange']
ball=turtle.Turtle()
ball.shape('square')
ball.color(random.choice(ball_colors))
ball.shapesize(stretch_len=1,stretch_wid=1)
ball.up()
ball.goto(0,0)
ball.down()
ball.showturtle()
ball.speed(0)
ball.dx=2
ball.dy=-2

pen=turtle.Turtle()
pen.color('black')
pen.up()
pen.goto(0,260)
pen.down()
pen.showturtle()
pen.write('PYPONG GAME',align='center',font=('Times New Roman',22,'bold'))
pen.up()
pen.goto(0,245)
pen.down()
pen.write('Created by PyDanny',align='center',font=('Times New Roman',9,'underline'))

pen.hideturtle()

pen1=turtle.Turtle()
pen1.color('black')
pen1.up()
pen1.goto(0,220)
pen1.down()
pen1.showturtle()
score=0
attempt=20
pen1.write(f'Score : {score}       Attempt : {attempt}',align='center',font=('Courier',15,'bold'))
pen1.hideturtle()

def paddle_a_up():
    y=paddle_a.ycor()
    y+=20
    paddle_a.up()
    paddle_a.sety(y)

def paddle_a_down():
    y=paddle_a.ycor()
    y-=20
    paddle_a.up()
    paddle_a.sety(y)

def paddle_b_up():
    y=paddle_b.ycor()
    y+=20
    paddle_b.up()
    paddle_b.sety(y)

def paddle_b_down():
    y=paddle_b.ycor()
    y-=20
    paddle_b.up()
    paddle_b.sety(y)

wn.listen()
wn.onkeypress(paddle_a_up,'q')
wn.onkeypress(paddle_a_down,'a')
wn.onkeypress(paddle_b_up,'o')
wn.onkeypress(paddle_b_down,'l')


while(True):
    wn.update()
    #move ball
    ball.up()
    ball.sety(ball.ycor()+ball.dy)
    ball.setx(ball.xcor()+ball.dx)

    #border check
    if ball.ycor()>=290:
        ball.sety(290)
        ball.dy=-1
    elif ball.ycor() <= -290:
        ball.sety(-290)
        ball.dy = 1
    elif ball.xcor() >= 390:
        ball.goto(0,0)
        ball.dx = -1
        pen1.clear()
        attempt-= 2
        pen1.write(f'Score : {score}       Attempt : {attempt}', align='center', font=('Courier', 15, 'bold'))

    elif ball.xcor() <= -390:
        ball.goto(0,0)
        pen1.clear()
        attempt-= 2
        pen1.write(f'Score : {score}       Attempt : {attempt}', align='center', font=('Courier', 15, 'bold'))

        if attempt==0:
            pen.up()
            pen.goto(0,0)
            pen.write('YOU LOSE!!!',align='center',font=('Times New Roman',22,'bold'))
            wn.exitonclick()
        ball.dy = -1


    #collision











        '''
        pen1.clear()
        score+=3
        pen1.write(f'Score:{score}')
'''


