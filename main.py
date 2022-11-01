import time
import turtle
from turtle import Screen
from blade import Blade
screen = Screen()
turtle.screensize(600,600)
screen.bgcolor("black")
screen.tracer(0)
bv = Blade()
cond = True
screen.listen()
bv.ball()
for i in range(2):
    screen.update()
    bv.players()
for m in range(2):
    bv.non()
while bv.cond is True:
    screen.update()
    screen.onkey(bv.forv, "Up")
    screen.onkey(bv.bacv, "Down")
    bv.ball()
    bv.brain()
while cond:
    screen.update()
    time.sleep(1)
    bv.score()
print("Game-Over")




screen.exitonclick()