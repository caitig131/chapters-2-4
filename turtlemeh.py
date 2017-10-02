import turtle
wn = turtle.Screen()
alex = turtle.Turtle()
alex.shape("turtle")
colors = ["red","blue","green","purple","pink","yellow","orange","magenta","lightgreen","grey"]
for color in colors:
    alex.color(color)
    alex.stamp()

    for i in range(4):
       alex.forward(100)
       alex.stamp()
       alex.left(90)
       print(i)
    alex.left(30)   
    
