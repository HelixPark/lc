
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)

        dp = [[0] * n for _ in range(n)]

        # base case
        for i in range(n):
            dp[i][i] = 1

        # 反着遍历保证正确的状态转移
        for i in range(n-1,-1,-1):
            for j in range(i+1,n,1):
                # 转移方程
                # 相等说明在同一个子序列里
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    # 不相等，则s[i + 1..j]和s[i..j - 1]谁的回⽂⼦序列更⻓？
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        # s的最长回文子串长度
        return dp[0][n-1]

s = 'bbbab'
c = Solution()
print(c.longestPalindromeSubseq(s))