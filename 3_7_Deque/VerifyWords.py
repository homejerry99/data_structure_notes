#我们尝试使用deque来进行回文词判定

import sys
sys.path.append('C:\\Users\\26066\\Desktop\\UM\\CISC\\PY_TEST\\3_5_DefineQueue')
sys.path.append('C:\\Users\\26066\\Desktop\\UM\\CISC\\PY_TEST\\3_6_PrinterQueue')
sys.path.append('C:\\Users\\26066\\Desktop\\UM\\CISC\\PY_TEST\\3_7_Deque')
print(sys.path)
import TestDeque

def verify(string):
    deque = TestDeque.TestDeque()
    stringList = list(string)
    for char in stringList:
        deque.addAtRear(char)
    while deque.size() > 1:
        f = deque.remveFromFront()
        r = deque.removeFromRear()
        if f != r:
            return False
    return deque.size() <= 1

print(verify('actva'))