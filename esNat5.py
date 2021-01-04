import turtle
import random
point = 0
snake = turtle.Turtle()
win = turtle.Screen()
mela = turtle.Turtle()
width=800
height=600
widthMela = 740
heightMela = 530
win.setup(width=width, height=height)
win.title("Snake")
win.bgcolor("green")
	
	
win.register_shape("melettaGiusta.gif")
mela.shape("melettaGiusta.gif")
mela.up()
snake.pencolor("blue")




def left():
	if snake.xcor() > -380:
		snake.setx(snake.xcor() - 10)
	else:
		win.bye()
	controllaMela()
	print(f"left {snake.pos()}")

def right():
	if snake.xcor() < 380:
		snake.setx(snake.xcor() + 10)
	else:
		win.bye()
	controllaMela()
	print(f"right {snake.pos()}")
	

def up():
	if snake.ycor() < 280:
		snake.sety(snake.ycor() + 10)
	else:
		win.bye()
	controllaMela()
	print(f"up {snake.pos()}")
	

def down():
	if snake.ycor() > -280:
		snake.sety(snake.ycor() - 10)
	else:
		win.bye()
	controllaMela()
	print(f"down {snake.pos()}")
    

def controllaMela():
	if snake.pos() == mela.pos():
		aggiungiMela(width,height)
		global point
		point = point + 1
		
		print("hello")
		print (point)
		


def aggiungiMela(width, height):
	x = random.randint(widthMela/2*-1, widthMela/2)//10 *10
	y = random.randint(heightMela/2*-1, heightMela/2)//10 *10
	mela.hideturtle()
	mela.setx(x)
	mela.sety(y)
	mela.showturtle()
	

def disegnaQuadrato():
	snake.begin_fill()
	for i in range(4):
		snake.forward(15)
		snake.left(90)
	snake.end_fill()

def main():

	aggiungiMela(width,height)
	snake.shape("square")
	snake.penup()
	win.onkey(left,"Left")
	win.onkey(right,"Right")
	win.onkey(up,"Up")
	win.onkey(down,"Down")
	win.listen()
	win.mainloop()
	
	print(f"Hai perso: hai fattp {point} punti")


	
if __name__ == "__main__":
	main()
