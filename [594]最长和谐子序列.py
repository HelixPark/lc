
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        # 哈希表存储数组中元素出现的次数，
        # 遍历hash,如果当前元素+1也在hash里面,计算两者次数之和,保留最大

        dicts = {}
        # 存次数
        for i in nums:
            dicts[i] = dicts.get(i,0)+1
        # 或者换成一下代码,一键转换为字典
        # dicts = collections.Counter(nums)

        res = 0
        for i in dicts:
            if i+1 in dicts:
                res = max(res,dicts[i]+dicts[i+1])
        return res