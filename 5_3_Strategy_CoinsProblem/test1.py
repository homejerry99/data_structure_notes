'''
因为贪心法不一定总是能找到最好方案，我们要继续来以硬币找零问题为例探索其他
首先是递归方案

最简单的情况，就是剩余的钱等于某个硬币面值。
而复杂的情况，我们可以通过一个一个拿硬币去试验，然后对余下的部分再做同方法，找出使余下部分的硬币数量最少的再加上，这么一层一层递归...

'''

import math
import time

def numberOfCoins(input,coinValuesList):
    #某种意义上使因为没有do while所以这么做？
    #初始把number设为输入钱数能够保证下面的第一次numberT的计算一定输入，之后后续就是比对numberT之间了
    number = input
    if input in coinValuesList:
        return 1
    else:
        #对每个面值进行计算，找其中最小的币数
        for coin in coinValuesList:
            if coin > input:
                continue
            numberT = 1 + numberOfCoins(input - coin,coinValuesList)
            if numberT < number:
                number = numberT
    return number

#n = numberOfCoins(52,[1,5,10,50])
#print(n)

'''
一个非常需要注意的事实是这么解的效率非常草生，很不实用
其原因就是巨大多的重复计算，例如我们总能很多次的重新计算某个尝试数值的硬币数
(也许我们应该把东西存起来然后在处理前直接调用一下...)
'''



def numberOfCoinsNEO(input, coinValuesList, dataDict):
    #某种意义上使因为没有do while所以这么做？
    #初始把number设为输入钱数能够保证下面的第一次numberT的计算一定输入，之后后续就是比对numberT之间了
    #储存并检查先前的内容
    number = input
    if input in coinValuesList:
        dataDict[input] = 1
        return 1
    elif dataDict.__contains__(input):
        return dataDict.get(input)
    else:
        #对每个面值进行计算，找其中最小的币数
        for coin in coinValuesList:
            if coin > input:
                continue
            tempValue = numberOfCoinsNEO(input - coin,coinValuesList,dataDict)
            numberT = 1 + tempValue
            if numberT < number:
                number = numberT
                dataDict[input] = number
    return number
data = {}
print(time.ctime())
n = numberOfCoinsNEO(244,[1,5,10,25,50],data)
print(n)
print(time.ctime())
print(data)

'''
这个技巧被称为函数值缓存或记忆化方法，相当程度的提升了递归的性能（）
当然你肯定会得到一个很大的缓存就是...空间换时间aya
'''