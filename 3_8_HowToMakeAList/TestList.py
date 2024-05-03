'''
前面能用list实现那么多劲爆的东西
但是我们很多时候却不一定有list...
我们需要学习list

list是一种数据集合，数据按照相对顺序排列（特别称之为unordered list，无序表）
其特点就是元素只有index（角标数字），要找其中的某个元素只能按照对应角标找

一个常规的list就像下面这样
'''

import sys
sys.path.append('C:\\Users\\26066\\Desktop\\UM\\CISC\\PY_TEST\\3_5_DefineQueue')
sys.path.append('C:\\Users\\26066\\Desktop\\UM\\CISC\\PY_TEST\\3_6_PrinterQueue')
sys.path.append('C:\\Users\\26066\\Desktop\\UM\\CISC\\PY_TEST\\3_7_Deque')
sys.path.append('C:\\Users\\26066\\Desktop\\UM\\CISC\\PY_TEST\\3_8_HowToMakeAlist')
print(sys.path)
import TestNode
#其实还需要注意，这里采用链接方式构建list（链表），实际上还可以直接通过数组构建list，将节点储存在数组中
class TestList():
    def __init__(self):
        self.head = None
    '''
    add和append和insert在添加的位置有很大的区别...
    pop和remove也是这样...
    反正add仅仅只是添加一个元素进入list...
    那自然的我们应该选择最方便的位置（是的，显然是head
    '''    
    def add(self,item):
        temp = TestNode.TestNode(item)
        temp.setNext(self.head)
        self.head = temp
    #remove自然也应该是从更方便的地方remove...
    #但是这个还挺需要技巧的...
    #仍然是遍历找到对应元素，但这一次我们需要调整被remove的元素两边元素的关系
    #两个部分，一个遍历找到对应的节点和前一个节点
    #另一部分负责把这个位置跳过去，即remove
    def remove(self,item):
        current = self.head
        previous = None
        found = False
        #find
        while not found and current != None:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
            #remove，注意中间和首位的remove的区别
        if current != None:
            if previous == None:
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext())
    #虽然很乐，但是这个确实是tm的靠遍历...
    def contain(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found
    def isEmpty(self):
        return self.head == None
    def size(self):
        #简单的计数
        count = 0
        current = self.head
        while current != None:
            count = count + 1
            current = current.getNext()
        return count
    def append(self,item):
        temp = TestNode.TestNode(item)
        temp.setNext(None)
        current = self.head
        previous = None
        while current != None:
            previous = current
            current = current.getNext()
        if previous != None:
            previous.setNext(temp)
    def index(self,item):
        current = self.head
        count = 0
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                count = count + 1
                current = current.getNext()
        return count
    
    def insert(self,pos,item):
        temp = TestNode.TestNode(item)
        temp.setNext(None)
        current = self.head
        previous = None
        found = False
        count = 0
        while not found and current != None:
            if count >= pos:
                if previous == None:
                    temp.setNext(current)
                    current = temp
                else:
                    previous.setNext(temp)
                    temp.setNext(current)
                found = True
            else:
                count = count + 1
                previous = current
                current = current.getNext()
                    
    def popLast(self):
        return self.pop(self.size()-1)
    #我想大家都应该记得indexOutOfBound这个异常（对于insert和pop
    def pop(self,pos):
        current = self.head
        count = 0
        found = False
        while not found and current != None:
            if count >= pos:
                self.remove(current.getData())
                found = True
            else:
                count = count + 1
                current = current.getNext()
        if current != None:      
            return current.getData()
        else:
            return None
    
'''
list数据的保存一定要保证相对位置的正确，但是并不一定需要绝对位置都是连续的（针对电脑本身
为了实现这种表，我们采取链表的形式（也就是把数据存储的空间按顺序链接，并且这些分布的数据在存储空间中并不一定相邻
明确需要标记的数据是末尾和开头的两个（head与end
我们使用节点Node来组成链表
每个Node至少包含一个数据项和指向下一个节点的引用信息（也就是下个节点是什么

根据以上信息，我们发现因为每个node均定义了next那么我只要找到最开始的node就能找到整个list的其他剩余部分
因此我们显然在init的时候需要给定一个head
另外，当head节点为空时，因为节点之间的链接特性，这个list一定是空的
'''