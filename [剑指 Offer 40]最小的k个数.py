# 输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。 
# 
#  
# 
#  示例 1： 
# 
#  输入：arr = [3,2,1], k = 2
# 输出：[1,2] 或者 [2,1]
#  
# 
#  示例 2： 
# 
#  输入：arr = [0,1,2,1], k = 1
# 输出：[0] 
# 
#  
# 
#  限制： 
# 
#  
#  0 <= k <= arr.length <= 10000 
#  0 <= arr[i] <= 10000 
#  
#  Related Topics 堆 分治算法 
#  👍 137 👎 0


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k == 0:
            return []
        import heapq
        # 先把前几个放进最大堆,建立堆
        queue = [-x for x in arr[:k]]
        heapq.heapify(queue)

        for i in range(k,len(arr)):
            # 当前元素比大堆堆顶小，则替换
            if -queue[0] > arr[i]:
                heapq.heapreplace(queue,-arr[i])

        res = [-x for x in queue]
        return res