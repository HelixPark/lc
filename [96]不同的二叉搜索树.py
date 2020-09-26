
class Solution:
    def numTrees1(self, n: int) -> int:
        # dp
        dp = [0] * (n+1)
        dp[0], dp[1] = 1, 1
        # 依次遍历每个节点
        for i in range(2,n+1):
            for j in range(1,i+1):
                dp[i] += dp[j-1]*dp[i-j]
        return dp[n]
    def numTrees2(self, n: int) -> int:
        # 递归:超时
        if n == 0 or n == 1:
            return 1
        num = 0
        for i in range(1,n+1):
            num += self.numTrees(i-1) * self.numTrees(n-i)
        return num
