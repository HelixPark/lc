from typing import List

class Solution:
    def subarraySum1(self, nums: List[int], k: int) -> int:

        l = len(nums)
        sum = [0] * (l + 1)
        # 构建前缀和
        for i in range(l):
            sum[i+1] = sum[i] + nums[i]

        # 穷举所有子数组:双重循环超时，就用hash存
        res = 0
        for i in range(1, l+1):
            for j in range(0, i):
                if sum[i] - sum[j] == k:
                    res += 1

        return res

    def subarraySum(self, nums: List[int], k: int) -> int:
        # 穷举所有子数组:双重循环超时，就用hash存
        # 使用前缀和方式
        size = len(nums)
        res, sum0_i = 0, 0

        hashDict = {}   #前缀和 ：出现次数（和lc1一样）
        hashDict[0] = 1

        for i in range(0,size):
            sum0_i += nums[i]       # nums[0:i]的前缀和
            sum0_j = sum0_i - k
            # 如果hash里这个前缀和，直接更新,
            if sum0_j in hashDict:
                res += hashDict[sum0_j]
            # 把前缀和nums[0..i]加⼊并记录出现次数否则添加到里面
            hashDict[sum0_i] = hashDict.get(sum0_i,0) + 1

        return res

nums = [1,1,1]
k = 2

c = Solution()
print(c.subarraySum(nums,k))