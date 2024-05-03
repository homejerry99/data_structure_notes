import random

class PrinterTask:
    def __init__(self,time):
        #反正只是模拟试验，所以我们直接的在实例化的时候就自己random Pages了
        self.pages = random.randrange(1,21)
        self.timeStamp = time
    def getPages(self):
        return self.pages
    def getTimeStamp(self):
        return self.timeStamp
    def getWaitingTime(self,currentTime):
        return currentTime - self.timeStamp

def newPrinterTask():
    #按照概率生成
    num = random.randrange(1,181)
    if num == 66:
        return True
    else:
        return False