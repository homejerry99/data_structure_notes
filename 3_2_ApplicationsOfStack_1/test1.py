#我们尝试使用Stack这个结构来匹配字符串的括号(判断括号是否成对)
#具体就是直接将从固定方向(左到右)遍历字符，发现左括号之后将数据压入栈，发现右括号将对应的数据从栈顶移除
#至于压进去的是什么似乎不用在意...
import sys
sys.path.append('C:\\Users\\26066\\Desktop\\UM\\CISC\\PY_TEST\\3_1_DefineStack')
import TestStack

def parChecker(string):
    stack = TestStack.TestStack()
    stringList = list(string)
    for i in range(len(string)):
        if stringList[i] == '(':
            stack.push(stringList[i])
        elif stringList[i] == ')':
            if stack.isEmpty():
                return False
            else:
                stack.pop()
    
    return stack.isEmpty()

print(parChecker('((()))'))
print(parChecker('((())'))
print(parChecker('())'))

#这就是圆括号本身的匹配了
        
