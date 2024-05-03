#使用stack来实现十进制->二进制
#算法上来说，我们是将十进制数不断除以2，所得余数从右到左排列(低位到高位)，最后得到一个二进制数
#stack的特性，最先压入的离顶端最远很符合这个特性(次序反转)

import sys
sys.path.append('C:\\Users\\26066\\Desktop\\UM\\CISC\\PY_TEST\\3_1_DefineStack')
import TestStack

def DecimalToBinary(number):
    stack = TestStack.TestStack()
    while number > 0:
        rem = number % 2
        stack.push(rem)
        number = number//2
        #余数除法和整数除法在Python中的方便表示
    outputString = ""
    while not stack.isEmpty():
        outputString = outputString + str(stack.pop())

    return outputString

print(DecimalToBinary(233))

#这个算法很容易的改几个参数就能用来转换其他进制(求其他的余数)