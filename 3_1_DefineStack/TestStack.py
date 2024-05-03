class TestStack:
    #Python中的类的首个参数是是实例对象本身，称为self
    #self.items表示的是一个List
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items) - 1]
    def size(self):
        return len(self.items)
    
#这样就做成了一个Stack

#Stack是一种线性的结构，一种数据集合
#Stack是有次序的，数据进出的一端为Top，另一端为Base
#Stack中数据的加入与移除均在Top，使得数据的进出呈现出Last In First Out的特性
#一种常见的场景就是浏览器的后退功能和历史记录，以及ctrl+Z
#我们可以自己定义一种具有这些性质的类(Class)

#这个类应当包含的操作首先应该有创建一个空的Stack，Stack()
#然后就是压入和取出数据的操作，push(item)和pop()
#peek()用于检视顶端到底是什么
#isEmpty()方便的用于确定是否是Empty的函数
#size()方便的确定到底有多少元素(数据项)的函数

#Stack本身也是一个数据集合，所以我们用Python自带的List类型可以定义这么一个东西
#将List的尾部，编号为-1的位置作为top，这样的话就可以用List本身的函数来进行push和pop

#另外像数组和链表这些，也是数据结构，可以按照类似的方式构造类(当然使用的就是更基本的东西了)
#这里的这些list等等是语言本身内置已经构造好的数组和链表
#可能像C这种老东西会因为默认没有这个(emmm，瞎猜的，其实我也不知道有没有)会让你更容易理解这是个需要去构造的东西...