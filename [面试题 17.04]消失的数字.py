# 数组nums包含从0到n的所有整数，但其中缺了一个。请编写代码找出那个缺失的整数。你有办法在O(n)时间内完成吗？ 
# 
#  注意：本题相对书上原题稍作改动 
# 
#  示例 1： 
# 
#  输入：[3,0,1]
# 输出：2 
# 
#  
# 
#  示例 2： 
# 
#  输入：[9,6,4,2,3,5,7,0,1]
# 输出：8
#  
#  Related Topics 位运算 数组 数学 
#  👍 18 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def missingNumber1(self, nums: List[int]) -> int:
        # 放入hash查询，时间空间o(n),
        hashSet = set()
        for i in nums:
            hashSet.add(i)
        for i in range(len(nums)+1):
            if i not in hashSet:
                return i
    def missingNumber(self, nums: List[int]) -> int:
        # 等差数列
        n = len(nums)
        # 公式：(⾸项+ 末项) * 项数/ 2
        sum = (0 + n) * (n + 1) / 2

        res = 0
        for i in nums:
            res += i
        return int(sum - res)

