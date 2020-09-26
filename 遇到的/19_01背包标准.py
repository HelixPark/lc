# -*- coding:utf-8 -*-
import sys
K = int(input())
N = int(input())

line = sys.stdin.readline().strip()
values = list(map(int, line.split()))
w = values
line = sys.stdin.readline().strip()
values = list(map(int, line.split()))
v = values

# K, N = 9, 5
# w = [2,2,4,6,3]
# v = [3,4,8,9,6]
# 标准模板
def bag(n,c,w,v):
    # n = 6  物品的数量，
    # c = 10 书包能承受的重量，
    # w = [2, 2, 3, 1, 5, 2] 每个物品的重量，
    # v = [2, 3, 1, 5, 4, 3] 每个物品的价值
    # dp[i][j]表示在面对第i件物品，且背包容量为j时所能获得的最大价值
    dp = [[0] * (c+1) for _ in range(n+1)]

    for i in range(1,n+1):
        for j in range(1,c+1):
            # 能装的下:装或者不装
            if j >= w[i]:
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-w[i]]+v[i])
            else:
                # 装不下
                dp[i][j] = dp[i-1][j]
    return dp[n][c]

def traceback(dp,n,c):
    # 找到装了几个物品
    res = [0] * (n+1)
    for i in range(n,1,-1):
        # 说明有没有第n件物品都一样
        if dp[i][c] == dp[i-1][c]:
            res[i] = 0
        else:
            res[i] = 1
            c -= w[i-1]
    if dp[1][c] > 0:
        res[1] = 1
    else:
        res[1] = 0
    # 1表示拿，0表示不拿
    print(res)

def bag1(n, c, w, v):
    """
    测试数据：
    n = 6  物品的数量，
    c = 10 书包能承受的重量，
    w = [2, 2, 3, 1, 5, 2] 每个物品的重量，
    v = [2, 3, 1, 5, 4, 3] 每个物品的价值
    """
    # 置零，表示初始状态
    # dp[i][j]表示在面对第i件物品，且背包容量为j时所能获得的最大价值
    value = [[0 for j in range(c + 1)] for i in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, c + 1):
            # 容量放不下时
            value[i][j] = value[i - 1][j]
            # 背包总容量够放当前物体，遍历前一个状态考虑是否置换
            if j >= w[i - 1] and value[i][j] < value[i - 1][j - w[i - 1]] + v[i - 1]:
                value[i][j] = value[i - 1][j - w[i - 1]] + v[i - 1]
    for x in value:
        print(x)
    return value[n][c]

print(bag(N,K,w,v))