import turtle
wn = turtle.Screen()
caitlin = turtle.Turtle()
caitlin.shape("turtle")
caitlin.speed(10)
colors = ["red","blue","green","purple","pink","yellow","orange","magenta","lightgreen","grey","aqua","brown","black","hotpink","darkgreen","lightyellow","darkorange","violet"]
for color in colors:
    caitlin.color(color)
    caitlin.stamp()

    for i in range(6):
       caitlin.forward(100)
       caitlin.stamp()
       caitlin.left(100)
       print(i)
    caitlin.left(100)   
    