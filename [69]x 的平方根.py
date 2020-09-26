# 实现 int sqrt(int x) 函数。 
# 
#  计算并返回 x 的平方根，其中 x 是非负整数。 
# 
#  由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。 
# 
#  示例 1: 
# 
#  输入: 4
# 输出: 2
#  
# 
#  示例 2: 
# 
#  输入: 8
# 输出: 2
# 说明: 8 的平方根是 2.82842..., 
#      由于返回类型是整数，小数部分将被舍去。
#  
#  Related Topics 数学 二分查找 
#  👍 510 👎 0


class Solution:
    def mySqrt1(self, x: int) -> int:
        # 二分法
        left, right = 0, x
        res = -1
        while left <= right:
            mid = (left + right) // 2
            if mid * mid <= x:
                res = mid
                left = mid + 1
            else:
                right = mid - 1
        return res
    def mySqrt(self, x: int) -> int:
        # 牛顿迭代
        if x == 0:
            return 0
        c, x0 = float(x), float(x)
        while True:
            xi = 0.5 * (x0 + c / x0)
            if abs(x0-xi) < 1e-7:
                break
            x0 = xi
        return int(x0)