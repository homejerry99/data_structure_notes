'''
先定义好迷宫class
我们需要将一个txt的字符迷宫变成变成更能被接受的东西
使用list的list来描述迷宫
比如一行就是一个list元素，然后整个迷宫从上到下有这么多行
'''
import turtle
class Maze():
    def __init__(self,mazeFileName):
        self.t = turtle.Turtle()
        rowsInMaze = 0
        columnsInMaze = 0
        self.mazeList = []
        mazeFile = open(mazeFileName,"r")
        #非常传统的按照行和列遍历
        for line in mazeFile:
            lineChars = []
            columnSize = 0
            for char in line[:-1]:
                lineChars.append(char) 
                if char == "S":
                    self.startRow = rowsInMaze
                    self.startColumn = columnSize
                columnSize = columnSize + 1
            rowsInMaze = rowsInMaze + 1
            self.mazeList.append(line)
            #所以无论如何都是方的了...
            columnsInMaze = len(self.mazeList) 
    
    def drawMaze(self):
        
    #用于更新海龟位置并标记此前的路径
    def updateMaze(self,turtle,val):
        
    def isExit(self,turtle):
        
        
                