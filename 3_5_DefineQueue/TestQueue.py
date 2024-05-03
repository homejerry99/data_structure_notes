#队列Queue和Stack一样，是一种数据集合，同样是一种线性的结构，有首位两端，数据的移除只允许在首端(front)，而数据加入仅允许在尾端(rear)
#具有先进先出的特性
#实际例子很多.aya
#我们可以定义一个类来实现这种结构
#在python中我们仍然使用List来实现

class TestQueue():
    def __init__(self):
        self.items = []
    def enqueue(self,item):
        self.items.append(item)
    def dequeue(self):
        return self.items.pop(0)
    def size(self):
        return len(self.items)
    def isEmpty(self):
        return self.items == []
    

