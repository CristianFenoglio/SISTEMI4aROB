import turtle

robot = turtle.Turtle()
win = turtle.Screen()


def sin(d):
    if robot.xcor() >= -380:
        robot.setx(robot.xcor() - 10)
        #if robot.xcor()<0 and d:
        #    d=False
        #    s=True
        #    robot.left(90)
    

def des(s):
    if robot.xcor() <= 380:
        robot.setx(robot.xcor() + 10)
        #if robot.xcor()>0 and s:
        #    d=True
        #    s=False
        #    robot.left(90)
    

def sopr():
    if robot.ycor() <= 380:
        robot.sety(robot.ycor() + 10)
    

def sott():
    if robot.ycor() >= -380:
        robot.sety(robot.ycor() - 10)


'''
def controllo():
    ok=False
    if int(robot.xcor())<380:
        if int(robot.ycor())<380:
            if int(robot.xcor())>-380:
                if int(robot.ycor())>-380:
                    ok=True
    
    return ok



def sin():
    if controllo():
        robot.backward(50)

def des():
    if controllo():
        robot.forward(50) 
 
def sopr():
    if controllo():
        robot.left(90)
        robot.forward(50)
        robot.right(90)



def sott():
    if controllo():
        robot.right(90)
        robot.forward(50)
        robot.left(90)

'''

win.title("My game")
win.bgcolor("green")
win.setup(width=800, height=800)
d=True
s=True
win.listen() #mette la finestra in ascolto di eventi (es: pressione tasti)
win.onkey(sin(d), "a")
win.onkey(des(s), "d")
win.onkey(sott, "s")
win.onkey(sopr, "w")
win.mainloop()