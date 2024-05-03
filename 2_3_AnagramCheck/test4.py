#记录每个单词中各个字母出现的次数，如果两个单词各个字母的出现次数相等，则是变位词
#26个字母每一个都整一个计数器(草)
#也许会更方便?

def checkNumberOfLetters(string1,string2):
    c1 = [0]*26 #26位的计数器
    c2 = [0]*26
    for i in range(len(string1)):
        pos = ord(string1[i]) - ord("a") #python的字母顺序位置计算，对应位数的ord减去字母表开头a的ord
        c1[pos] = c1[pos] + 1
    for i in range(len(string2)):
        pos = ord(string2[i]) - ord("a") #python的字母顺序位置计算，对应位数的ord减去字母表开头a的ord
        c2[pos] = c2[pos] + 1
    j = 0
    checkFailure = False
    while j < 26 and not checkFailure:
        if c1[j] != c2[j]:
            checkFailure = True
        else:
            j = j + 1
    return checkFailure

print(checkNumberOfLetters("abcd","cbda"))

#看起来只有O(n)，性能优秀!
#代价是一个26位的计数器...空间增大了（中文字库警告）
#空间换时间和时间换空间是常用的算法设计
#ord返回的是unicode的编码
    