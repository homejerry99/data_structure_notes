#前面的list是无序表
#现在我们来考虑另一种List，有序表，其中数据的顺序是由data的大小决定的
#同样使用Node来实现
import sys
sys.path.append('C:\\Users\\26066\\Desktop\\UM\\CISC\\PY_TEST\\3_5_DefineQueue')
sys.path.append('C:\\Users\\26066\\Desktop\\UM\\CISC\\PY_TEST\\3_6_PrinterQueue')
sys.path.append('C:\\Users\\26066\\Desktop\\UM\\CISC\\PY_TEST\\3_7_Deque')
sys.path.append('C:\\Users\\26066\\Desktop\\UM\\CISC\\PY_TEST\\3_8_HowToMakeAlist')
import TestNode
#仍然采用一个head来索引可以直接用常规的list同款
#对于那些和次序无关的的方法，都可以采用和之前一样的方式
class TestOrderdList():
    def __init__(self):
        self.head = None
        
    #按顺序add.png
    def add(self,item):
        current = self.head
        previous = None
        found = False
        temp = TestNode.TestNode(item)
        while not found and current != None:
            if current.getData() > item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if found:
            if previous != None:
                temp.setNext(current)
                previous.setNext(item)
            else:
                temp.setNext(self.head)
                self.head = temp
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
    def contain(self,item):
        #有序表的有序特性让我们可以更快的确定元素是否在集合内
        #由于将data按照从小到大的顺序排列，因此当对应位置节点的data大于需要查找的data时，后续一定没有我们所找的东西，那么就一定是False
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()
        return found
        
    def isEmpty(self):
        return self.head == None
    def size(self):
        count = 0
        current = self.head
        while current != None:
            count = count + 1
            current = current.getNext()
        return count
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
    #def append(self,item):
    #def insert(self,pos,item):
    #有序表不需要手动定位，所以只有一种add来添加元素   
    def popLast(self):
        return self.pop(self.size()-1)
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
        
        #我们发现链表的head很多时候都需要特殊考虑（