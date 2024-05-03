#先前已经将中缀表达式转换为了后缀表达式，接下来我们要开始计算后缀表达式，这个过程仍然需要使用stack的特性
#例如ABC*+，我们按顺序读取，先将A压入，然后再接着压入B和C，直到读取到*的时候，从顶端按顺序取出C和B并计算得出结果，再将这个结果压回去，之后读到+，就可以用这个结果和A来计算最终了

import sys
sys.path.append('C:\\Users\\26066\\Desktop\\UM\\CISC\\PY_TEST\\3_1_DefineStack')
import TestStack
def getValue(expression):
    stack = TestStack.TestStack()
    expressionTokens = expression.split()

    for token in expressionTokens:
        if token in '0123456789':
            stack.push(int(token))
        else:
            T1 = stack.pop()
            T2 = stack.pop()
            result = doMath(token,T1,T2)
            stack.push(result)
    
    return stack.pop()

def doMath(operator,T1,T2):
    if operator == '+':
        return T1 + T2
    if operator == '-':
        return T1 - T2
    if operator == '*':
        return T1 * T2
    if operator == '/':
        return T1 * T2
    
print(getValue("0 12 9 * +"))