# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。 
# 
#  
# 
#  示例： 
# 
#  输入：n = 3
# 输出：[
#        "((()))",
#        "(()())",
#        "(())()",
#        "()(())",
#        "()()()"
#      ]
#  
#  Related Topics 字符串 回溯算法 
#  👍 1320 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # dfs1：官方
        ans = []
        def backtrack(S, left, right):
            if len(S) == 2 * n:
                ans.append(''.join(S))
                return
            if left < n:
                # 左括号数量小于n，可以放一个左括号
                S.append('(')
                backtrack(S, left + 1, right)
                S.pop()
            if right < left:
                # 如果右括号数量小于左括号的数量，我们可以放一个右括号
                S.append(')')
                backtrack(S, left, right + 1)
                S.pop()

        backtrack([], 0, 0)
        return ans
    def generateParenthesis2(self, n: int) -> List[str]:
        # DFS2：
        res = []
        cur_str = ''
        def dfs(cur_str, left, right):
            """
            :cur_str: 从根结点到叶子结点的路径字符串
            :left: 左括号还可以使用的个数
            :right: 右括号还可以使用的个数
            """
            if left == 0 and right == 0:
                res.append(cur_str)
                return
            if right < left:
                return
            if left > 0:
                dfs(cur_str + '(', left - 1, right)
            if right > 0:
                dfs(cur_str + ')', left, right - 1)

        dfs(cur_str, n, n)
        return res

    def generateParenthesis3(self, n: int) -> List[str]:
        # DP：dp[i]：使用 i 对括号能够生成的组合。
        # dp[i] = "(" + dp[j] + ")" + dp[i - j - 1], j = 0, 1, ..., i - 1
        if n == 0:
            return []

        dp = [None for _ in range(n + 1)]
        dp[0] = [""]

        for i in range(1, n + 1):
            cur = []
            for j in range(i):
                left = dp[j]
                right = dp[i - j - 1]
                for s1 in left:
                    for s2 in right:
                        cur.append("(" + s1 + ")" + s2)
            dp[i] = cur
        return dp[n]
