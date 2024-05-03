#通过将两个词按照字母顺序排序看最后是否相等来比较判断是否为变位词
#直接使用内置函数sort...
def checkTheOrder(string1,string2):
    string1List = list(string1)
    string2List = list(string2)
    string1List.sort()
    string2List.sort()
    checkFailure = False
    pos = 0
    while not checkFailure and pos < len(string1):
        if string1List[pos] != string2List[pos]:
            checkFailure = True
        else:
            pos = pos + 1
    return checkFailure

print(checkTheOrder("abcd","bbda"))

#此算法的主导在内置的sort上(python,很神奇吧)
#其时间复杂度大概是O(n*logn)
#神奇的内置.png