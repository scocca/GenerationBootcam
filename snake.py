import turtle
import time
from random import randrange, choice


wn=turtle.Screen()
wn.title("sanke")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

cordx=randrange(-380, 380)
cordy=randrange(-280, 280)

food=turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("white")
food.penup()
food.goto(cordx, cordy)

snake=turtle.Turtle()
snake.speed(0)
snake.shape('square')
snake.color('white')
snake.penup()
snake.goto(0,0)
snake.direction = "stop"

def movement():
    if snake.direction=="up":
        y=snake.ycor()
        snake.sety(y+20)

    if snake.direction=="down":
        y=snake.ycor()
        snake.sety(y-20)

    if snake.direction=="right":
        x=snake.xcor()
        snake.setx(x+20)

    if snake.direction=="left":
        x=snake.xcor()
        snake.setx(x-20)

def movUp():
    if snake.direction!="down":
        snake.direction="up"

def movDown():
    if snake.direction!="up":
        snake.direction="down"

def movRight():
    if snake.direction!="left":
        snake.direction="right"

def movLeft():
    if snake.direction!="right":
        snake.direction="left"


wn.listen()
wn.onkeypress(movUp, "Up")
wn.onkeypress(movDown, "Down")
wn.onkeypress(movLeft, "Left")
wn.onkeypress(movRight, "Right")


size=[]
size.append(snake)
gameOver=False

while gameOver==False:
    movement()
    wn.update()
    totalSize=len(size)
   
    if len(size)>1:
        for i in range (1, totalSize):
            sx=snake.xcor()
            sy=snake.ycor()

            if size[i].xcor()==sx and size[i].ycor()==sy:
                gameOver=True
                turtle.done()
                break

    if(food.xcor()-12<=snake.xcor()<=food.xcor()+12 and
        food.ycor()-12<=snake.ycor()<=food.ycor()+12):
        x=snake.xcor()
        y=snake.ycor()

        newPart=turtle.Turtle()
        newPart.speed(0)
        newPart.shape("square")
        newPart.color("white")
        newPart.penup()
        newPart.goto(x,y)

        size.append(newPart)

        cordx=randrange(-380, 380)
        cordy=randrange(-280, 280)

        occupied=True

        while occupied:
            cordx=randrange(-380, 380)
            cordy=randrange(-280, 280)
            occupied=any(abs(turtle.ycor() - cordy) < 20 for turtle in size) or any(abs(turtle.xcor() - cordx) < 20 for turtle in size)

        food.goto(cordx,cordy)

    

    for i in range (totalSize-1, 0, -1):
        x = size[i-1].xcor()
        y = size[i-1].ycor()
        size[i].goto(x,y)
    

    if snake.xcor()>385:
        gameOver=True
        turtle.done()
        #snake.goto(-385, snake.ycor())
    
    if snake.xcor()<-385:
        gameOver=True
        turtle.done()
    
    if snake.ycor()>285:
        gameOver=True
        turtle.done()
    
    if snake.ycor()<-285:
        gameOver=True
        turtle.done()

    time.sleep(0.05)
    