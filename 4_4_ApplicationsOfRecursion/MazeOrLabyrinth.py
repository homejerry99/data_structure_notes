#使用递归来解决迷宫
#并没有做完...
import Maze
import turtle
m = Maze.Maze("testMaze.txt")
print(m.mazeList)
t = turtle.Turtle()
def getOutOfHere(maze):
    