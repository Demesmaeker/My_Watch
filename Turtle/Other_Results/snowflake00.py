import turtle
import time
times=time.perf_counter()
def koch(size,n):
    if n==0:
        turtle.fd(size)
    else:
        for angle in [0,60,-120,60]:
            turtle.left(angle)
            koch(size/3,n-1)

def main():
    global times
    turtle.speed("fastest")
    turtle.setup(600,600)
    turtle.penup()
    turtle.goto(-200,100)
    turtle.pendown()
    turtle.pensize(2)
    level=4   # This is the number of Koch curves
    koch(400,level)
    turtle.rt(120)
    koch(400,level)
    turtle.rt(120)
    koch(400,level)
    turtle.hideturtle()
    
    text = turtle.Turtle() 
    text.color("black") 
    text.penup() 
    text.setposition(0, 0) 
    text.write("Joyeux Noël", font=("Apple Chancery", 20, "bold"), align="center") 
    text.setposition(0, -30) 
    text.color("dark green") 
    text.write("de BeCode", font=("Avenir", 20, "bold"), align="center") 
     
    text.hideturtle() 

    turtle.done()

main()

