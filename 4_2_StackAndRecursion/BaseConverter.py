#尝试使用递归的算法进行进制转换
#目的是10进制转换到16以内的任意进制

#从最开始最简单的时候看，也就是number小于base，此时可以直接对应位数
#更复杂的情况，需要连续的除以base，得到的整除答案重新进行BaseConverter
#于是这就是递归了！

def BaseConverter(number,base):
    digts = '0123456789ABCDEF'
    output = ''
    if number < base:
        output = str(digts[number]) + output
    else:
        remainder = number % base
        number = number // base
        output = BaseConverter(number = number,base = base) + str(digts[remainder]) + output
    
    return output

print(BaseConverter(255,16))

'''
下面来解释解释为什么可以递归
当一个函数被调用时，系统将会把调用时的现场数据压入系统调用栈（一个特殊的stack）
每次调用时压入stack的现场数据称为栈帧
函数return的时候，从stack的顶部取得数据，将栈帧返回到原先的地址
而这里整个过程我们最终会调用到那个最简单的结果，然后这个结果会给到下一层还没出来的现场数据，这样一层一层返回，最终把底端的返回就是我们要的最终结果

现场数据，包含了要返回的函数名称，要返回的数据类型，调用时输入的参数和函数运行内部的所有东西

调试递归时会遇到一些独特的错误，比如RecursionError
这个错误表示递归的层数太多了（）超出了stack
需要检查你的终止条件（）

python中的sys模块（你import的那个）可以对递归深度（也就是层数）进行调整

sys.getrecursionlimit()
可以赋值
sys.setrecursionlimit(3000)
'''