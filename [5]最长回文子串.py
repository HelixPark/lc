# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。 
# 
#  示例 1： 
# 
#  输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
#  
# 
#  示例 2： 
# 
#  输入: "cbbd"
# 输出: "bb"
#  
#  Related Topics 字符串 动态规划 
#  👍 2436 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def check(self,s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            # 向两边展开
            left -= 1
            right += 1

        # 返回以s[l]和s[r]为中⼼的最⻓回⽂串
        return s[left + 1: right]

    def longestPalindrome1(self, s: str) -> str:
        # 核⼼思想是：从中间开始向两边扩散来判断回⽂串.中心扩散法
        res = ''
        for i in range(len(s)):
            # 以s[i]为中心的 最长回文子串
            s1 = self.check(s, i, i)
            # 以s[i] s[i+1]为中心的 最长回文子串
            s2 = self.check(s, i, i+1)

            if len(res) < len(s1):
                res = s1
            if len(res) < len(s2):
                res = s2
        return res

    def longestPalindrome(self, s: str) -> str:
        # dp：dp[i,j]表示s[i:j]是否为回文子串
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        res = ''
        # 枚举子串的长度 k+1:主要是为了排除小于2长度的子串
        for k in range(n):
        #  枚举子串的起始位置 i，这样可以通过 j=i+l 得到子串的结束位置
            for i in range(n):
                j = i + 1
                if j >= len(s):
                    break
                # 字符串长度为1
                if k == 0:
                    dp[i][j] = True
                # 字符串长度为2
                elif k == 1:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (dp[i+1][j-1] and s[i] == s[j])

                if dp[i][j] and k + 1 > len(res):
                    res = s[i:j+1]
        return res


s = "babad"
c = Solution()
print(c.longestPalindrome(s))