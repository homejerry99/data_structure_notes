#中缀操作符的表达式对于计算机内部表达来说相当不方便
#解决的方案是使用前缀或者后缀表达式
#我们使用stack来将中缀表达式变成前缀或者后缀表达式
#先从全括号的中缀表达式开始，这种表达式直接用括号来表示所有操作的顺序

#举例来说，(A+(B*C))，转换为后缀表达，首先将内层的'('删除，然后'*'移动到')'这样内部的(B*C)就变成了BC*这样的后缀表达，得到(A+BC*)
#然后对外层的'('删除，'+'移动到右侧括号位置，变为ABC*+
#类似的也可以整出前缀表达式

#于是显然的，我们可以将所有的常规中缀表达式转化为括号中缀表达，然后用此算法转为前缀或后缀
#使用stack的原因是我们发现操作符输出顺序是反转的(见上例)
#同时对于括号，如(A+B)*C，转化为AB+C*，可以发现'+'输出的更早，整个过程是先把+放到右侧括号位置，然后再删除左括号(所以因为这个后删除的特性，也需要用stack暂存前括号)

#此算法中，中缀表达式默认由空格隔开的一些了token组成，操作符单词是各个单字的'+','-','*','/','(',')'(所以我们会先把字符串裂开.aya)
import sys
sys.path.append('C:\\Users\\26066\\Desktop\\UM\\CISC\\PY_TEST\\3_1_DefineStack')
import TestStack
def FormatTransform(string):
    perc = {}
    perc['*'] = 3
    perc['/'] = 3
    perc['+'] = 2
    perc['-'] = 2
    perc['('] = 1
    stack = TestStack.TestStack()
    outputList = []
    stringToken = string.split()

    #整体上是先把操作数和操作符分开，操作符总是需要先进stack调整顺序以便最终输出(把stack的内容直接丢到输出list末尾)
    for token in stringToken:
        if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or token in '0123456789':
            outputList.append(token)
        elif token == '(':
            stack.push(token)
        #下面的操作是在读取到右侧括号的时候，从stack中将剩余的东西取出(因为stack的特性顺序一定是符合后缀表达的)直到左括号(其实就是把两个括号之间的优先计算部分提前加入)
        elif token == ')':
            top = stack.pop()
            while top != '(':
                outputList.append(top)
                top = stack.pop()
        else:
            #对于剩下的操作符，需要比对stack顶端的操作符优先级，如果是顶端优先级高于或等于自己，立刻将顶端的算符加入输出尾部，直到遇见比自己低的，然后再把自己压入stack

            while (not stack.isEmpty() and perc[stack.peek()] >= perc[token]): #实际上网课上的解法是直接用数字来分级，加减为2级，乘除为3级，左括号为1级，于是大于等于2，也就是'('之外的所有...
                    outputList.append(stack.pop())
            stack.push(token)
    
    while not stack.isEmpty():
        outputList.append(stack.pop())

    return " ".join(outputList)

print(FormatTransform("A + B * C"))
print("A + B * C".split())
#正则表达式是很神奇的东西，记得输入的时候要加空格哦(也就是A+B*C是不会分开的，但是A + B * C可以)

