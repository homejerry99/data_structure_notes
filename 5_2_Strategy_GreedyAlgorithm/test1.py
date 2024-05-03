'''
贪心策略，指在解决问题的过程中的每一步都取局部最优解，然后最终将其拼成最终解
在将大的问题分成小的问题时，如果小的问题的最优能导出大的最优，这就是个相当方便优秀的方法

此策略一般是最容易想到的，不过其实他也不总是能得到最优解，比如硬币面值体系诡异的情况...

这里我们来用此方法来解决找零问题，也就是让找零的硬币数量最少
最直观的方法，使用贪心策略，先用最大面值最多数量占据最大部分，然后对剩下的部分重复同样操作
'''

def greedy(inputMoney):
    #不同硬币数量
    P50N = 0
    P25N = 0
    P10N = 0
    P5N = 0
    P1N = 0
    #硬币面值
    P50 = 50
    P25 = 25
    P10 = 10
    P5 = 5
    P1 = 1
    
    P50N = inputMoney // P50
    inputMoney = inputMoney % P50
    P25N = inputMoney // P25
    inputMoney = inputMoney % P25
    P10N = inputMoney // P10
    inputMoney = inputMoney % P10
    P5N = inputMoney // P5
    inputMoney = inputMoney % P5
    P1N = inputMoney // P1
    
    print("50 cents : %d \n" %P50N)
    print("25 cents : %d \n" %P25N)
    print("10 cents : %d \n" %P10N)
    print("5 cents : %d \n" %P5N)
    print("1 cents : %d \n" %P1N)
    
greedy(132)
    