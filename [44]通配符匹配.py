
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m,n=len(s),len(p)
        # 创建动态规划矩阵
        dp=[[bool(False) for i in range(n+1)] for j in range(m+1)]
        dp[0][0]=True

        # 初始化填充，如果s为空的话，只有*的模式才能匹配
        for i in range(n):
            if dp[0][i] and p[i] == '*':
                dp[0][i+1]=True

        for i in range(1,m+1):
            for j in range(1,n+1):
                if p[j-1] == '*':
                    dp[i][j] = dp[i][j-1] or dp[i-1][j]
                elif p[j-1] == '?' or s[i-1] == p[j-1]:
                    dp[i][j] = dp[i-1][j-1]
        return dp[m][n]