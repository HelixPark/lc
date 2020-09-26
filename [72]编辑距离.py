

class Solution:
    def minDistance1(self, word1: str, word2: str) -> int:
        # 这里把word1变为word2(目标)

        def dp(i,j):
            # base case，就是哪个先走完
            if i == -1: return j+1
            if j == -1: return i+1

            if word1[i] == word2[j]:
                # 啥都不做，skip
                return dp(i-1, j-1)
            else:
                return min(
                    dp(i, j-1)+1,   #插入
                    dp(i-1, j)+1,     #删除
                    dp(i-1, j-1) + 1    #替换
                )
        # i, j初始化指向最后一个指引
        return dp(len(word1)-1, len(word2)-1)

    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        # 有一个字符串为空
        # 有一个长度为0
        if n * m == 0:
            return n + m

        dp = [ [0] * (m+1) for _ in range(n+1)]

        for i in range(n+1):
            dp[i][0] = i
        for j in range(m+1):
            dp[0][j] = j

        # for i in range(1, n+1):
        #     for j in range(1, m+1):
        #         left = dp[i-1][j] + 1
        #         down = dp[i][j-1] + 1
        #         left_down = dp[i-1][j-1]
        #
        #         if word1[i-1] != word2[j-1]:
        #             left_down += 1
        #         dp[i][j] = min(left, down, left_down)
        for i in range(1,n+1):
            for j in range(1,m+1):
                tmp = 0
                if word1[i-1] != word2[j-1]:
                    tmp = 1
                dp[i][j] = min(dp[i-1][j] + 1, #增加
                               dp[i][j-1] + 1, #删除
                               dp[i-1][j-1] + tmp) #替换

        return dp[n][m]


