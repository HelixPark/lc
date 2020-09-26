
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        if len(text1) == 0 or len(text2) == 0:
            return 0
        # m+1 * n+1数组
        dp = [[0] * (n+1) for i in range(m+1)]

        for i in range(1,m+1):
            for j in range(1,n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
                    # dp[i][j] = 0 #最长公共子串，只需修改这一行
        return dp[m][n]

text1 = 'abcde'
text2 = 'ace'

c = Solution()
c.longestCommonSubsequence(text1,text2)