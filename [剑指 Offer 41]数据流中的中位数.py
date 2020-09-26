# 如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，那么中位数就是所有数
# 值排序之后中间两个数的平均值。 
# 
#  例如， 
# 
#  [2,3,4] 的中位数是 3 
# 
#  [2,3] 的中位数是 (2 + 3) / 2 = 2.5 
# 
#  设计一个支持以下两种操作的数据结构： 
# 
#  
#  void addNum(int num) - 从数据流中添加一个整数到数据结构中。 
#  double findMedian() - 返回目前所有元素的中位数。 
#  
# 
#  示例 1： 
# 
#  输入：
# ["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]
# [[],[1],[2],[],[3],[]]
# 输出：[null,null,null,1.50000,null,2.00000]
#  
# 
#  示例 2： 
# 
#  输入：
# ["MedianFinder","addNum","findMedian","addNum","findMedian"]
# [[],[2],[],[3],[]]
# 输出：[null,null,2.00000,null,2.50000] 
# 
#  
# 
#  限制： 
# 
#  
#  最多会对 addNum、findMedian 进行 50000 次调用。 
#  
# 
#  注意：本题与主站 295 题相同：https://leetcode-cn.com/problems/find-median-from-data-strea
# m/ 
#  Related Topics 堆 设计 
#  👍 66 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class MedianFinder:

    def __init__(self):
        # 当前大顶堆和小顶堆的元素个数之和
        self.count = 0
        self.max_heap = []  #用于存储较小一半数字的大顶对
        self.min_heap = []  #用于存储较大一半数字的小顶对

    def addNum(self, num: int) -> None:
        # 从数据流中添加一个整数到数据结构中
        import heapq
        self.count += 1
        # 先放进大堆（相反数），再大堆弹出最大的到小堆（为了平衡）
        heapq.heappush(self.max_heap, -num)
        max_heap_top = heapq.heappop(self.max_heap)
        heapq.heappush(self.min_heap, -max_heap_top)

        # 小堆可能会多一个元素，再弹出来放到大堆。这俩步骤确保两个堆能够平衡
        if len(self.min_heap) > len(self.max_heap):
            min_heap_top = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -min_heap_top)

    def findMedian(self) -> float:
        # - 返回目前所有元素的中位数
        if self.count % 2 == 1:
        # if self.count & 1:
            # 如果两个堆合起来的元素个数是奇数，数据流的中位数大顶堆的堆顶元素
            return -self.max_heap[0]
        else:
            # 如果两个堆合起来的元素个数是偶数，数据流的中位数就是各自堆顶元素的平均值
            return (self.min_heap[0] - self.max_heap[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# leetcode submit region end(Prohibit modification and deletion)
