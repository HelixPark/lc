# 给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。 
# 
#  示例 1: 
# 
#  输入: "(()"
# 输出: 2
# 解释: 最长有效括号子串为 "()"
#  
# 
#  示例 2: 
# 
#  输入: ")()())"
# 输出: 4
# 解释: 最长有效括号子串为 "()()"
#  
#  Related Topics 字符串 动态规划 
#  👍 981 👎 0


class Solution:
    def longestValidParentheses1(self, s: str) -> int:
        # dp：dp[i] 表示以下标i字符结尾的最长有效括号的长度
        size, res = len(s), 0
        dp = [0] * size

        for i in range(1,size):
            if s[i] == ')':
                # "()这种"
                if s[i-1] == '(':
                    if i >= 2:
                        dp[i] = dp[i-2]+2
                    else:
                        dp[i] = 0 + 2
                # (...))这种
                elif (i-dp[i-1]) > 0 and s[i-dp[i-1]-1] == '(':
                    if i - dp[i-1] >= 2:
                        dp[i] = dp[i-1] + dp[i-dp[i-1]-2] + 2
                    else:
                        dp[i] = dp[i-1] + 2
                res = max(res, dp[i])
        return res
    def longestValidParentheses(self, s: str) -> int:
        # 栈的方式
        # 遇到的（我们将它的下标放入栈中
        # 遇到的‘)’，先弹出栈顶元素表示匹配了当前右括号
        res, stack = 0, []
        # 防止第一个左括号入栈后，后期不满足{最后一个没有被匹配的右括号下标}
        stack.append(-1)
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i) #下标入栈
            else:
                # 先弹出栈顶元素表示匹配了当前右括号
                stack.pop()
                if not stack:
                    # ruo栈为空，说明当前的右括号为没有被匹配的右括号，
                    # 将其下标放入栈中来更新之前提到的「最后一个没有被匹配的右括号的下标」
                    stack.append(i)
                else:
                    # ruo栈不为空，当前右括号的下标减去栈顶元素即为
                    # 「以该右括号为结尾的最长有效括号的长度」
                    res = max(res, i - stack[-1])
        return res
s = ")()())"
c = Solution()
c.longestValidParentheses(s)