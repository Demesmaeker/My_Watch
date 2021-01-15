import turtle

# Caroline is a turtle
caroline = turtle.Turtle()
caroline.shape('turtle')
caroline.color('red')
caroline.pensize(5)
caroline.speed(1)

# Caroline can move
caroline.forward(100)
caroline.left(90)
caroline.forward(100)
caroline.right(90)

# # caroline can change
caroline.speed(3)
caroline.color('green')

# # Caroline can stop drawing
caroline.penup()
caroline.backward(100)
caroline.right(90)
caroline.pendown()
caroline.forward(100)

# # Caroline can have a friend
atome = turtle.Turtle()
atome.color('blue')
atome.pensize(20)
atome.backward(100)


turtle.done()