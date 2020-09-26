# -*- coding:utf-8 -*-

# 洗牌算法：利用随机出的index下标对应的数，与数组从前到后相互切换，所以称为洗牌，
# 随机选择两个位置，将两个位置上的值交换
# 代码运行效率相比前面几种高，随机性也很大

data = [1,2,3,4,5,6,7,8,9]
import random

def fun(data):
    size = len(data)
    for i in range(size):
        # 随机产生0到size-1的索引号
        index1 = random.randint(0,size-1)  #两边均为闭区间
        index2 = random.randint(0,size-1)
        # 然后交换
        data[index1], data[index2] = data[index2], data[index1]
fun(data)


