# 找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。 
# 
#  说明： 
# 
#  
#  所有数字都是正整数。 
#  解集不能包含重复的组合。 
#  
# 
#  示例 1: 
# 
#  输入: k = 3, n = 7
# 输出: [[1,2,4]]
#  
# 
#  示例 2: 
# 
#  输入: k = 3, n = 9
# 输出: [[1,2,6], [1,3,5], [2,3,4]]
#  
#  Related Topics 数组 回溯算法 
#  👍 156 👎 0

from typing import List
class Solution:
    def combinationSum3_1(self, k: int, n: int) -> List[List[int]]:
        res = []

        def dfs(num, s, tmp):
            # 数组长度大于k或者之和大于n，不符合要求，返回
            if len(tmp) > k or s > n:
                return
            # 满足要求
            if len(tmp) == k and s == n:
                res.append(tmp[:])
                return
            for i in range(num+1, 10):
                # 剪枝，s + i > n说明后面的说斗大于n
                if s + i > n:
                    break
                dfs(i, s+i, tmp+[i])
        dfs(0,0,[])
        return res
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # 回溯，没剪枝
        res, tmp = [], []

        def dfs(k,n,index):
            if k == 0:
                if n == 0:
                    res.append(tmp[:])
                return
            i = index
            while i <= 9 and n-i>=0:
                tmp.append(i)
                dfs(k-1,n-i,i+1)
                tmp.pop()
                i += 1
        dfs(k,n,1)
        return res

c = Solution()
print(c.combinationSum3(3,9))