#fractal，分形，是我们熟悉的一个数学名词
#其通常的定义为：一个粗糙或零碎的几何形状，可以分成数个部分，且每一部分都（至少近似地）是整体缩小后的形状
#显然，递归这种自己调自己的和这个有点概念上的神似
#我们将用图像来展现递归
#使用经典的海龟作图工具
import turtle

'''
t = turtle.Turtle()
t.forward(100)
turtle.done()
'''

def drawATree(branchLength):
    if branchLength > 5:
        t.forward(branchLength)
        t.left(30)
        drawATree(branchLength-20)
        t.right(60)
        drawATree(branchLength-20)
        t.left(30)
        t.backward(branchLength)
     
t = turtle.Turtle()
t.left(90)
t.penup()
t.backward(100)
t.pendown()    
t.pencolor('green')
t.pensize(2)
drawATree(100)
t.hideturtle()
turtle.done()
    
        