'''
现在我们开始对算法进行分析
首先来看顺序查找
也就是按顺序从开始遍历到结尾直到出现我们所需要的东西

目标随机出现在序列里，最好情况比对1次，最差比对n次，而如果不存在则一定要比对n次，因此平均的查找是n/2次，于是复杂度是O(n)

而如果是有序表，最好是1次，最差是n次，而不存在时可以根据排序情况减少查询次数，两个都是平均n/2次，复杂度仍然是O(n)
'''