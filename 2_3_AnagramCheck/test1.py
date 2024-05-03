#目的是实现通过检查两个字符串之间每个字母的匹配来确定是否为变位词
#为了防止重复检查需要再检查string2的时候将对应的单字标记(相当于划去，但是位置还是占位的)，这需要将string2转为List
def checkEveryLetter(string1,string2):
    pos1 = 0
    string2List = list(string2)
    checkFailure = False
    while not checkFailure and pos1 < len(string1):
        pos2 = 0
        found = False
        while not found and pos2 < len(string2):
            if string1[pos1] == string2List[pos2]:
                string2List[pos2] = None
                found = True
            else:
                pos2 = pos2 + 1
        if not found:
            checkFailure = True
        else:
            pos1 = pos1 + 1
    return checkFailure

print(checkEveryLetter("miss","sism"))

#总执行次数为(1+2+...+n)=1/2(n)(n+1)
#内层循环的次数每一次都在减少.aya
#时间复杂度O(n^2)
            
