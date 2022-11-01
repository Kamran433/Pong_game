from turtle import Turtle, Screen
import random


class Blade:
    def __init__(self):
        self.jok = Turtle()
        self.jol = Turtle()
        self.score1 = 0
        self.score2 = 0
        self.y = random.randint(-250, 250)
        self.screen = Screen()
        self.timmy = Turtle()
        self.john = Turtle()
        self.jimmy = Turtle()
        self.kimmy = Turtle()
        self.nohn = Turtle()
        self.nimmy = Turtle()
        self.pl = [self.timmy, self.john, self.jimmy]
        self.pr = [self.kimmy, self.nohn, self.nimmy]
        self.loll = Turtle()
        self.players()
        self.bechy = Turtle()
        self.non()
        self.cond = True
        self.ball()
        # self.screen.tracer(0)


    def players(self):
        self.loll.shape("square")
        self.loll.color("white")
        self.loll.shapesize(0.5, 0.5)
        self.loll.penup()
        self.loll.goto(self.pl[1].xcor() + 20, self.pl[1].ycor())
        self.loll.setheading(30)
        for i in range(3):
          # self.screen.update()
          self.pr[i].shape("square")
          self.pr[i].color("white")
          self.pr[i].penup()
          self.pr[i].goto(333, 20*i)
          self.pl[i].shape("square")
          self.pl[i].color("white")
          self.pl[i].penup()
        self.pl[0].goto(-345, self.y)
        self.pl[1].goto(-345, self.y - 20)
        self.pl[2].goto(-345, self.y - 40)
    def forv(self):
        self.pr[0].setheading(90)
        self.pr[1].setheading(90)
        self.pr[2].setheading(90)
        for i in range(3):
            # self.screen.update()
            self.pr[i].speed("fastest")
            self.pr[i].forward(40)
            # self.screen.update()

    def bacv(self):
        self.pr[0].setheading(270)
        self.pr[1].setheading(270)
        self.pr[2].setheading(270)
        for i in range(3):
            # self.screen.update()
            self.pr[i].speed("fastest")
            self.pr[i].forward(40)
            # self.time.sleep(0.1)
            # self.screen.update()
    def mov(self):
      self.bechy.setheading(90)
      for _ in range(30):
          self.bechy.forward(20)
          self.bechy.penup()
          self.bechy.forward(10)
          self.bechy.pendown()
    def non(self):
        self.bechy.shape("square")
        self.bechy.color("white")
        self.bechy.penup()
        self.bechy.goto(0,-350)
        self.bechy.pendown()
        self.bechy.shapesize(0.05, 0.05)
        self.mov()
    def ball(self):
        # self.loll.speed("normal")
        self.jok.color("white")
        self.jok.hideturtle()
        self.jok.penup()
        self.jok.goto(-150, 280)
        self.jol.color("white")
        self.jol.hideturtle()
        self.jol.penup()
        self.jol.goto(150, 280)
        self.jol.write(f"{self.score1}", align="right", font=("Arial", 50, "normal"))
        self.jol.clear()
        self.jok.write(f"{self.score2}", align="left", font=("Arial", 50, "normal"))
        self.jok.clear()
        if self.loll.ycor() >= 300:
            self.loll.setheading(-self.loll.heading())
        elif self.loll.distance(self.pr[0]) <= 22 or self.loll.distance(self.pr[1]) <= 22 or self.loll.distance(self.pr[2]) <= 22:
           self.loll.setheading(self.loll.heading() - 90)
           self.loll.speed() * 0.9
           self.score1 += 1
        elif self.loll.distance(self.pl[0]) <= 19 or self.loll.distance(self.pl[1]) <= 19 or self.loll.distance(self.pl[2]) <= 19:
            self.loll.setheading(self.loll.heading() + 90)
            self.loll.speed() * 0.9
            self.score2 += 1
        elif self.loll.ycor() <= -300:
            self.loll.setheading(-self.loll.heading())
        elif self.loll.xcor() <= -345 or self.loll.xcor() >= 333:
            self.cond = False
        self.loll.forward(10)


    def brain(self):
        self.pl[0].goto(-345, self.loll.ycor())
        self.pl[1].goto(-345, self.loll.ycor() - 20)
        self.pl[2].goto(-345, self.loll.ycor() - 40)