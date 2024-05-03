#一个有用的实例，用来学习如何建模
#具体场景复述：
#实验室中任意1h内有10名学生在场，在这1h内每个人将发起2次打印，每次1到20页
#打印机有两种形式：快速模式，低质量，每分钟10张，质量模式，高质量，每分钟5张
#问题：在大家都不会等很久的情况下尽力提高打印质量
#这是一个决策问题，直接算显然不那么方便，所以我们要建模模拟，再根据情况决策
#step1：抽象，我们将这个问题抽象，去除无关部分，得到以下的对象和过程
#对象：
#打印任务：属性为1.提交时间和2.打印数量
#打印队列：一个普通的队列，元素是打印任务
#打印机：一个打印机，有两个状态（是否在忙），以及打印速度属性
#过程：
#1.生成和提交打印任务：按照已知的信息来模拟生成与提交打印任务，所有都按均匀分布
#此时可得1h内将有20个任务，每秒出现新任务的概率为1/180
#而同时每次任务将有1到20页，于是每次任务的页数X自然是离散的随机变量，P(X = a) = 1/20，任务页数为a的概率是1/20
#2.打印机处理打印任务：打印机读取队列首位的任务属性，然后按照速率处理掉任务
#简单的按照速率减少页数即可，当页数归0，dequeue，然后加载下一个任务
#我们需要同步所有的过程，均匀的流逝时间（everyFrame！）显然打印机和任务生成都是每帧在做的

#最终，整体上，我们的模拟有3个大步骤
#1.创建打印队列对象（就像信网络的任务刷新队列
#2.不断地生成打印任务和处理打印任务（每帧）
#清晰的过程，每帧概率生成任务进入队列，打印机自动处理队列首位的任务，当队列空了则打印机空闲
#要点是要记录每个任务的等待时间，并计算出平均等待时间（这里我们记录生成任务时的时间，再用执行的时间点减去来得到每个任务对应的时间

#这里就是核心的模拟文件(CoreCycle?)
import sys
sys.path.append('C:\\Users\\26066\\Desktop\\UM\\CISC\\PY_TEST\\3_5_DefineQueue')
sys.path.append('C:\\Users\\26066\\Desktop\\UM\\CISC\\PY_TEST\\3_6_PrinterQueue')
sys.path.append('C:\\Users\\26066\\.vscode\\extensions\\ms-python.vscode-pylance-2023.8.40\\dist\\bundled\\stubs\\matplotlib\\pyplot.pyi')
print(sys.path)
import TestQueue
import Printer
import PrinterTask
def advance(totalTimes,pagesPerMinute):
    queue = TestQueue.TestQueue()
    printer = Printer.Printer(pagesPerMinute)
    totalWaitingTimes = []

    for currentSecond in range(totalTimes):
        if PrinterTask.newPrinterTask():
            task = PrinterTask.PrinterTask(currentSecond)
            queue.enqueue(task)
        if not printer.isBusy() and not queue.isEmpty():
            newTask = queue.dequeue()
            printer.beginNewTask(newTask)
            totalWaitingTimes.append(newTask.getWaitingTime(currentSecond))
        printer.printTask()
    
    averageWaitingTime = sum(totalWaitingTimes)/len(totalWaitingTimes)
    print('Average wait %6.2f sec, %3d tasks remaining'% (averageWaitingTime,queue.size()))
    return averageWaitingTime

print(advance(3600,5))