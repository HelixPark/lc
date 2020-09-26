# -*- coding:utf-8 -*-
# 如果⼀个数如果只能被1和它本⾝整除，那么这个数就是素数

# 返回区间[2, n) 中有⼏个素数
def isPrimes(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
def countPrimes(n):
    # 基础解法
    res = []
    for i in range(2,n):
        if isPrimes(i):
            res.append(i)
    return res

def countPrimes2(n):
    # 高效解法：Sieve of Eratosthenes
    # O(N * loglogN)
    isPrim = [True] * n
    i = 2
    while (i * i) < n:
        if isPrim[i]:
            # i的倍数不可能是素数了
            j = 2 * i
            while j < n:
                isPrim[j] = False
                j = j + i

        i += 1
    count = 0
    for i in range(2,n):
        if isPrim[i]:
            count += 1
    return count

print(countPrimes(10))
print(countPrimes2(10))