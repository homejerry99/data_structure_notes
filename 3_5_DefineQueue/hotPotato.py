#简单的尝试解决一下热土豆
#目的是传土豆直到一定的次数再剔除当时拿到土豆的人
#输入时一个人名list，而输出应当是剩余的人（固定传递次数或传递到仅剩一人）
#队列在此处的优势就是可以把队首的remove再加回到队尾（于是变成一圈了）
#这样队首始终持有土豆，当次数到了的时候remove队首但是不加回去

import sys
sys.path.append('C:\\Users\\26066\\Desktop\\UM\\CISC\\PY_TEST\\3_5_DefineQueue')
#注意下python的导入...或者说没有用IDE而是直接搓代码总是会遇到这种问题呢emmm
#Python的Package就是文件夹啦
import TestQueue

def getTheLastOne(nameList,passTime):

    queue = TestQueue.TestQueue()
    for k in nameList:
        queue.enqueue(k)
    i = 0
    while queue.size() > 1:
        p = queue.dequeue()
        i = i + 1
        if(i < passTime):
            #print(queue)
            queue.enqueue(p)
        else:
            i = 0
    return queue.dequeue()

test = list(range(1,32))
print(test)
print(getTheLastOne(test,7))
