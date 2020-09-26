# -*- coding:utf-8 -*-

# 动态规划:从左上走到右下，只能向下或者向右
def fun(n,m):
    dp = [[0] * m for _ in range(n)]
    for i in range(n):
        dp[i][0] = 1
    for j in range(m):
        dp[0][j] = 1
    for i in range(1,n):
        for j in range(1,m):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[n-1][m-1]

print(fun(2,3))

# 递归形式：可以看成深度遍历
def fun2(n,m):
    count = 0
    if n == 1 and m == 1:
        return 1
    if n > 1:
        count += fun2(n-1,m)
    if m > 1:
        count += fun2(n,m-1)
    return count
print(fun2(2,3))
