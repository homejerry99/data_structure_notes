import sys
sys.path.append('C:\\Users\\26066\\Desktop\\UM\\CISC\\PY_TEST\\3_1_DefineStack')
import TestStack

#为了判断多种括号的情况，需要检查括号类型
def parChecker(string):
    stack = TestStack.TestStack()
    stringList = list(string)
    for i in range(len(string)):
        symbol = stringList[i]
        
        if symbol in '([{':
            stack.push(stringList[i])
        elif symbol in ')]}':
            if stack.isEmpty():
                return False
            elif check(stack.peek(),symbol):
                stack.pop()
            else:
                return False
    
    return stack.isEmpty()

#'([{'和')]}'两个可以看成list，在对应标号的符号是对应的，我们单独写一个判断函数
def check(open,close):
    opens = '([{'
    closes = ')]}'
    return opens.index(open) == closes.index(close)

print(parChecker('{[({}{)}]'))
#这两个test的写法上可能都有些不太标准，可能直接像课上用while会比较好...
#但是只要增加一个括号检查就很方便呢.aya

#这种方法显然可以直接用在html和json之类的东西上(层次结构化文档.aya)