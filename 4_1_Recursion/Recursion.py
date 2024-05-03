#递归
#和数学归纳法有些关系（）
#具体的思想就是把大的问题分解为同类的小问题，直到最小的最直接可以解决的问题
#我们下面用这个例子来看

#目标：对一个list的数求和，但是不使用循环

#这里是一种
def addLastTowNum(list):
    
    if not len(list) <= 1:
        a = list.pop()
        b = list.pop()
        list.append(a+b)
        addLastTowNum(list)
    return list

#更标准的写法
#将初始的和后续的递归分开写
def listSum(list):
    if(len(list) == 1):
        return list[0]
    else:
        return list[0] + listSum(list[1:])
    
    
t = [1,2,3,4,5,10]
p = list(range(1,50))
print(addLastTowNum(t))
print(listSum(t))
print(addLastTowNum(p))
print(listSum(p))

#下面我们来介绍递归算法的总结
#1.递归一定要有一个最简问题的解决（直接不用循环的结束
#2.递归算法一定要能减小问题规模，向最简靠拢
#3.递归算法必须调用自身
#当没那么容易理解的自身调用出现时，请画图或者放置