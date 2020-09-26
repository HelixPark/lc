# 给定一个非空的整数数组，返回其中出现频率前 k 高的元素。 
# 
#  
# 
#  示例 1: 
# 
#  输入: nums = [1,1,1,2,2,3], k = 2
# 输出: [1,2]
#  
# 
#  示例 2: 
# 
#  输入: nums = [1], k = 1
# 输出: [1] 
# 
#  
# 
#  提示： 
# 
#  
#  你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。 
#  你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。 
#  题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的。 
#  你可以按任意顺序返回答案。 
#  
#  Related Topics 堆 哈希表 
#  👍 524 👎 0

from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 方式1：自己写的，先用hash存数字再用小顶堆
        # python默认小顶堆，要实现大顶堆，把数据进堆的时候存成相反数就行
        hashDict = {}
        for i in nums:
            hashDict[i] = hashDict.get(i,0) + 1
        # 建立堆，导入堆
        import heapq
        queue, res = [], []
        for value, count in hashDict.items():
            heapq.heappush(queue,(-count,value))

        for i in range(k):
            tmp = heapq.heappop(queue)
            res.append(tmp[1])
        return res

    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        # 方式2：先用hash，再用小顶堆实现，python默认小顶堆，nlogk
        import collections
        dic = collections.Counter(nums)

        import heapq#使用堆（优先队列）
        queue, res = [], []
        for i in dic:
            heapq.heappush(queue, (-dic[i],i))
        for i in range(k):
            tmp = heapq.heappop(queue)
            res.append(tmp[1])

    def topKFrequent1(self, nums: List[int], k: int) -> List[int]:
        # 方式3：hash的方式，然后对dict字典排序，nlogn
        hashDict = {}
        for i in nums:
            hashDict[i] = hashDict.get(i,0) + 1
        key = sorted(hashDict.items(), key=lambda x : (x[1],x[0]) ,reverse=True)
        return [key[j][0] for j in range(k)]

nums = [3,1,1,1,2,2]
k = 2
c = Solution()
print(c.topKFrequent(nums,k))