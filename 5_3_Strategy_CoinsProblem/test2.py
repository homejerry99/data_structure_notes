'''
下面来说说动态规划的方法，同样以找零问题为例
思路是从最简单比如1的找零问题开始，逐步增加输入值直到得出最终所需结果
要保证每一次的递加都是最优的

应用此方法的核心在于问题的最优解包含更小规模的问题的最优解，这是问题能够被动态规划解决的必要条件
'''
import time

def numberOfCoins(inputNumber, coinValuesList, dataDict):
    i = 0
    while i < inputNumber:
        i = i + 1
        minCoinNumber = i
        if i in coinValuesList:
            dataDict[i] = 1
            continue
        for coinValue in coinValuesList:
            if coinValue > i:
                continue
            #逐步建立兑换表，从1开始aya
            coinNumber = 1 + dataDict[i - coinValue]
            if coinNumber < minCoinNumber:
                minCoinNumber = coinNumber
        dataDict[i] = minCoinNumber
    return dataDict[inputNumber]
    
data = {}
print(time.ctime())
n = numberOfCoins(244,[1,5,10,25,50],data)
print(n)
print(time.ctime())
print(data)

'''
此类方法的整体思路也是从小规模开始，但是是正向的，直接解出一个一个小问题的解并记录最终组合
每一步都依靠之前的最优得到这一次的最优
我们还可以对此方法扩展来得到硬币组成
在最优解生成的时候附带一个表记录下这一次增加的单个硬币面值，得到最终解后，减去本次选择的硬币币值回溯之前部分的找零所选，直到完全找完，这时就得到了整体用币的list
'''

def numberOfCoinsNEO(inputNumber, coinValuesList, dataDict, usedCoins):
    i = 0
    while i < inputNumber:
        i = i + 1
        minCoinNumber = i
        thisTimeCoin = 1
        if i in coinValuesList:
            dataDict[i] = 1
            usedCoins[i] = i
            continue
        for coinValue in coinValuesList:
            if coinValue > i:
                continue
            #逐步建立兑换表，从1开始aya
            coinNumber = 1 + dataDict[i - coinValue]
            if coinNumber < minCoinNumber:
                minCoinNumber = coinNumber
                thisTimeCoin = coinValue
                
        dataDict[i] = minCoinNumber
        usedCoins[i] = thisTimeCoin
    return dataDict[inputNumber]

def printCoins(usedCoins,inputNumber):
    v = inputNumber
    while v > 0:
        thisCoin = usedCoins[v]
        print(thisCoin)
        v = v - thisCoin
        
data = {}
used = {}
print(time.ctime())
n = numberOfCoinsNEO(244,[1,5,10,25,50],data,used)
print(n)
print(time.ctime())
printCoins(used,244)