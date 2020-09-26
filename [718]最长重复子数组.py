from typing import List
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        n, m = len(A), len(B)
        dp = [[0] * (m+1) for _ in range(n+1)]
        res = float('-inf')

        for i in range(0,n):
            for j in range(0,m):
                if A[i] == B[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = 0
                res = max(res, dp[i][j])
        return res

a = [1,2,3,2,1]
b = [3,2,1,4,7]
c = Solution()
print(c.findLength(a, b))