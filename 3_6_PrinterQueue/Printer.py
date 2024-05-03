
class Printer:
    def __init__(self,printSpeed):
        self.speed = printSpeed
        self.currentTask = None
        self.remainingTime = 0
    def isBusy(self):
        if self.currentTask != None:
            return True
        else:
            return False
    def printTask(self):
        #实际上，我们仅仅在接到新任务的时候直接计算打印预计的时间，然后直接等待时间结束...
        if self.currentTask != None:
            self.remainingTime = self.remainingTime - 1
            if self.remainingTime <= 0:
                self.currentTask = None
    def beginNewTask(self,newTask):
        if self.currentTask == None:
            self.currentTask = newTask
            self.remainingTime = (newTask.getPages())*60 / self.speed
    