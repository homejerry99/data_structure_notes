import turtle

t = turtle.Turtle()
def sierpinski(degree,points):
    colorMap = ['red','green','yellow','blue','white','orange']
    drawTriangle(points,colorMap[degree])
    if degree > 0:
        points1 = {
            'left':points['left'],
            'right':getMid(points['left'],points['right']),
            'top':getMid(points['left'],points['top'])
        }
        points2 = {
            'left':getMid(points['left'],points['right']),
            'right':points['right'],
            'top':getMid(points['right'],points['top'])
        }
        points3 = {
            'left':getMid(points['left'],points['top']),
            'right':getMid(points['right'],points['top']),
            'top':points['top']
        }
        sierpinski(degree - 1,points1)
        sierpinski(degree - 1,points2)
        sierpinski(degree - 1,points3)
    
    
def drawTriangle(points,color):
    t.fillcolor(color)
    t.penup()
    t.goto(points['left'])
    t.pendown()
    t.begin_fill()
    t.goto(points['right'])
    t.goto(points['top'])
    t.goto(points['left'])
    t.end_fill()
    
def getMid(pointA,pointB):
    return ((pointA[0] + pointB[0])*0.5,(pointA[1] + pointB[1])*0.5)

points = {
    'left':(0,0),
    'right':(400,0),
    'top':(200,340)
}

sierpinski(5,points)
turtle.done()

    