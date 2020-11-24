#roba a caso
#from turtle import *
import turtle
gigi=turtle.Turtle()
n=input("inserire il numero di lati: ")
n=int(n)
color('red', 'yellow')
begin_fill()
while True:
    gigi.forward(50)
    gigi.left(360/n)
    if abs(gigi.pos()) < 1:
        break
gigi.end_fill()

