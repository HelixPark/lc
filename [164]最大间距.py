# 给定一个无序的数组，找出数组在排序之后，相邻元素之间最大的差值。 
# 
#  如果数组元素个数小于 2，则返回 0。 
# 
#  示例 1: 
# 
#  输入: [3,6,9,1]
# 输出: 3
# 解释: 排序后的数组是 [1,3,6,9], 其中相邻元素 (3,6) 和 (6,9) 之间都存在最大差值 3。 
# 
#  示例 2: 
# 
#  输入: [10]
# 输出: 0
# 解释: 数组元素个数小于 2，因此返回 0。 
# 
#  说明: 
# 
#  
#  你可以假设数组中所有元素都是非负整数，且数值在 32 位有符号整数范围内。 
#  请尝试在线性时间复杂度和空间复杂度的条件下解决此问题。 
#  
#  Related Topics 排序 
#  👍 203 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        # 方式1，排序后，比较每两个之间的最大间隔，
        # 方式2：桶排序，下面就是桶排序

        if not nums or len(nums) < 2:
            return 0

        # 找出最大值和最小值
        maxValue = max(nums)
        minValue = min(nums)

        # 出现1,1,1,1的情况
        if minValue == maxValue:
            return 0
        # 桶的间距等于（最大-最小）//（长度-1）
        margin = max(1,(maxValue-minValue)//(len(nums)-1))
        # 桶的个数等于（最大-最小）//间距 +1
        bkt_size = (maxValue-minValue) // margin + 1

        # 初始化每个桶的最大值和最小值
        bkt_min = [float('inf')]*bkt_size
        bkt_max = [0] * bkt_size

        for num in nums:
            # 每个数字它所yao被放在哪个桶里，用(值 - 最小值) // 桶间距得到下标
            idx = (num - minValue) // margin
            # 放进去后更新最大值和最小值
            bkt_min[idx] = min(bkt_min[idx], num)
            bkt_max[idx] = max(bkt_max[idx], num)

        res = lastBktIdx = 0
        for i in range(1,bkt_size):
            # 桶里的最大最小值并没进行过改变，说明桶里没有元素，跳过
            if bkt_min[i] == float('inf') or bkt_max == 0:
                continue
            # res = 当前桶的最小值 - 上个桶的最大值，得到相邻元素间的最大差值
            res = max(res, bkt_min[i]-bkt_max[lastBktIdx])
            lastBktIdx = i
        return res

    def maximumGap2(self, nums: List[int]) -> int:
        # 桶排序方式2，简短版本
        maxValue = max(nums)
        minValue = min(nums)
        tmp = [[]] * (len(nums) + 1)
        for i in nums:
            idx = (i - minValue) * len(nums) // (maxValue - minValue)
            if len(tmp[idx]) > 0:
                tmp[idx][0] = min(i, tmp[idx][0])
                tmp[idx][1] = max(i, tmp[idx][1])
            else:
                tmp[idx] = [i, i]
        res = 0
        maxV = tmp[0][0]
        for i in tmp:
            if len(i) > 0:
                res = max(res, i[0] - maxV)
                maxV = i[1]
        return res
nums = [3, 4,8,11,9]  #结果4