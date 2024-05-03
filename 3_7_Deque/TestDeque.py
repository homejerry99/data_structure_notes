#Deque，双端队列，首尾都可以remove和add元素
#集成了stack和queue的优势
#不具有内在的先进后出（FILO）的特性和内在的先进先出（FIFO）特性，需要使用者自行维护（）
class TestDeque:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def addAtRear(self,item):
        self.items.append(item)
    def removeFromRear(self):
        return self.items.pop()
    def addAtFront(self,item):
        self.items.insert(item,0)
    def remveFromFront(self):
        return self.items.pop(0)
    def size(self):
        return len(self.items)
    