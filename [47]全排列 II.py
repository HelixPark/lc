# 给定一个可包含重复数字的序列，返回所有不重复的全排列。 
# 
#  示例: 
# 
#  输入: [1,1,2]
# 输出:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ] 
#  Related Topics 回溯算法 
#  👍 385 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(tmp):
            if len(tmp) == size:
                res.append(tmp)
                return

            for i in range(size):
                # i位置没有被访问过
                if not visited[i]:
                    if i > 0 and nums[i] == nums[i-1] and not visited[i-1]:
                        continue
                    visited[i] = True
                    backtrack(tmp+[nums[i]])
                    visited[i] = False

        size = len(nums)
        nums.sort()
        res, visited = [], [False] * size
        backtrack([])
        return res