'''
尝试使用递归方法解决汉诺塔问题
每个塔看起来都可以看成一个stack?
我们需要把stack1中的所有数据按照同样的顺序压入stack3

对于n层的塔，首先进行处理将最底层的数据先压入stack3，然后对剩余的数据执行n-1层的算法...
'''

import sys
sys.path.append('C:\\Users\\26066\\Desktop\\UM\\CISC\\PY_TEST\\3_1_DefineStack')
import TestStack
#1和3是输入和输出，而2是中间使用
def HanoiTowerDataTranpose(stack1,stack2,stack3,times):
    if times == 1:
        stack3.push(stack1.pop())
    else:
        #先把1的顶端n-1个转移到2
        HanoiTowerDataTranpose(stack1,stack3,stack2,times - 1)
        #print(stack1.items)
        #再把1的底部放置到3
        stack3.push(stack1.pop())
        #然后把2的n-1个移动到3
        HanoiTowerDataTranpose(stack2,stack1,stack3,times - 1)

stack1 = TestStack.TestStack()    
stack2 = TestStack.TestStack()    
stack3 = TestStack.TestStack()
for i in range(1,7):
    stack1.push(i) 

print(stack1.items)
print(stack3.items)
HanoiTowerDataTranpose(stack1,stack2,stack3,6)
print(stack1.items)
print(stack3.items)