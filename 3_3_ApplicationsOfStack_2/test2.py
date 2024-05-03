import sys
sys.path.append('C:\\Users\\26066\\Desktop\\UM\\CISC\\PY_TEST\\3_1_DefineStack')
import TestStack

#这个算法很容易的改几个参数就能用来转换其他进制(求其他的余数)
#只不过十六进制的时候要稍稍处理一下位数(0123456789ABCDEF)

def BaseConverter(number,base):
    digts = '0123456789ABCDEF'
    stack = TestStack.TestStack()
    while number > 0:
        rem = number % base
        stack.push(rem)
        number = number//base
    outputString = ""
    while not stack.isEmpty():
        outputString = outputString + str(digts[stack.pop()])
    return outputString

print(BaseConverter(54,16))
print(BaseConverter(233,2))
print(4077.6875*16)
print(BaseConverter(65243,16))
