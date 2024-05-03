import sys
sys.path.append('C:\\Users\\26066\\Desktop\\UM\\CISC\\PY_TEST\\3_1_DefineStack')
#注意下python的导入...或者说没有用IDE而是直接搓代码总是会遇到这种问题呢emmm
#Python的Package就是文件夹啦
import TestStack
stack = TestStack.TestStack()
print(stack.isEmpty())

stack.push("Ayayayaya")
stack.push("EMMMMMMM")
print(stack.isEmpty())
print(stack.peek())
print(stack.pop())
print(stack.peek())

