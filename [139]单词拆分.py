
from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # 动态规划，dp[i]表示前i个(包括i)字符能否拆成wordDict
        l = len(s)
        dp = [False] * (l + 1)

        # base case
        dp[0] = True

        for i in range(1,l+1):
            for j in range(i):

                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[l]
# p = 'aabbcc'
# print(p[1:4])

s = "applepenapple"
wordDict = ["apple", "pen"]
c = Solution()
print(c.wordBreak(s,wordDict))