'''
利用动态规划方法解决如何让有限的背包中装入价值最大的物件
整体思路是从最0开始建立每个背包大小数值中的最大价值，并用前面得到的结果来推出后面的
'''
import math
#首先是按照价值和质量建立map，但是编号比较方便...
#key是质量
tr = [
    None,
    [2,3],
    [3,4],
    [7,9],
    [8,10],
    [9,11]
]
#最大容量
M = 20
#初始化记忆表，应当是数组与数字的对应
memoryMap = {}
'''
我们需要知道这个函数的相关内容
整体是输入质量和物件表，输出最大的价值
物件表和质量是两层循环

'''
def maxValue(trMap,maxWeight,memoryMap):
    for i in range(maxWeight + 1):
        maxValueI = 0
        for j in range(len(trMap)):
            #按照编号顺序得到对应的物件，然后得到重量并检查，如果重量不通过，则归到前一号
            #没错，全是顺序拿取物件...
            if trMap[j] == None or i == 0:
                memoryMap[(j,i)] = 0
                continue
            elif trMap[j][0] > i:
                maxValueI = memoryMap[(j-1,i)]
            else :
                #当可以装下的时候，需要比对如果不装这一件（可能会装其他的）所能得到的最大以及本件价值+先前最优
                maxValueI = max(memoryMap[(j-1,i)],trMap[j][1] + memoryMap[(j-1,i-trMap[j][0])])
            memoryMap[(j,i)] = maxValueI
    
    return memoryMap[(len(trMap) - 1,maxWeight)]
m = maxValue(tr,M,memoryMap)
print(m)
print(memoryMap)

'''
递归和动态规划很相似（）
一个是从复杂开始一步一步调用简单的结果，最终得到复杂结果（递归
另一个是直接按顺序处理，直接处理到复杂的条件
'''
            
    