# 你和你的朋友，两个人一起玩 Nim 游戏：桌子上有一堆石头，每次你们轮流拿掉 1 - 3 块石头。 拿掉最后一块石头的人就是获胜者。你作为先手。 
# 
#  你们是聪明人，每一步都是最优解。 编写一个函数，来判断你是否可以在给定石头数量的情况下赢得游戏。 
# 
#  示例: 
# 
#  输入: 4
# 输出: false 
# 解释: 如果堆中有 4 块石头，那么你永远不会赢得比赛；
#      因为无论你拿走 1 块、2 块 还是 3 块石头，最后一块石头总是会被你的朋友拿走。
#  
#  Related Topics 脑筋急转弯 极小化极大 
#  👍 340 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def canWinNim1(self, n: int) -> bool:
        # 递归算法：超时
        if n <= 0:
            return False
        if n <= 3:
            # 必赢
            return True
        # 判断n-1,n-2,n-3是否会赢：有一个为true即能赢
        return self.canWinNim(n-1) == False or \
               self.canWinNim(n-2) == False or \
               self.canWinNim(n-3) == False

    def canWinNim2(self, n: int) -> bool:
        # 动态规划:超内存
        dp = [True] * n
        # 当n=0,1,2时，先手总会赢
        for i in range(3,n):
            dp[i] = dp[i-1] == False \
                    or dp[i-2] == False \
                    or dp[i-3] == False
        return dp[n-1]

    def canWinNim3(self, n: int) -> bool:
        # dp只需要三个存储空间，优化一下
        # 动态规划:内存小了，确超时eg：n = 1348820612
        dp = [True] * 3
        # 当n=0,1,2（也就是前三个子）时，先手总会赢
        res = True
        for i in range(3, n):
             res = dp[0] == False \
                    or dp[1] == False \
                    or dp[2] == False

             dp[0], dp[1], dp[2] = dp[1], dp[2], res
        return res

    def canWinNim(self, n: int) -> bool:
        # 一行
        # 如果石头数n不能被4整除，那么先手总是可以赢得
        return n % 4 != 0
        
# leetcode submit region end(Prohibit modification and deletion)
