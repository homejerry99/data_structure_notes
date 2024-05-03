#现在我们来建造一个Node类
#这就是list中元素的容器（？
#初始化时此实例将没有next
#我们将在List的实现中处理这些
class TestNode():
    def __init__(self,initData):
        self.data = initData
        self.next = None
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self,input):
        self.data = input
    def setNext(self,input):
        self.next = input
    