import sys
sys.path.append('C:\\Users\\26066\\Desktop\\UM\\CISC\\PY_TEST\\3_5_DefineQueue')
sys.path.append('C:\\Users\\26066\\Desktop\\UM\\CISC\\PY_TEST\\3_6_PrinterQueue')
sys.path.append('C:\\Users\\26066\\Desktop\\UM\\CISC\\PY_TEST\\3_7_Deque')
sys.path.append('C:\\Users\\26066\\Desktop\\UM\\CISC\\PY_TEST\\3_8_HowToMakeAlist')
print(sys.path)

import TestList

testList = TestList.TestList()

testList.add(34)
testList.add(233)
testList.append(666)
testList.insert(1,123)
print(testList.isEmpty())
print(testList.size())
print(testList.popLast())
print(testList.contain(233))
print(testList.index(123))