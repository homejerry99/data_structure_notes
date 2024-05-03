import sys
sys.path.append('C:\\Users\\26066\\Desktop\\UM\\CISC\\PY_TEST\\3_5_DefineQueue')
#注意下python的导入...或者说没有用IDE而是直接搓代码总是会遇到这种问题呢emmm
#Python的Package就是文件夹啦
import TestQueue
queue = TestQueue.TestQueue()

queue.enqueue('a')
queue.enqueue('233')
queue.enqueue('emmm')
print(queue.dequeue())
print(queue.dequeue())