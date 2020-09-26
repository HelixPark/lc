# 给你一个链表数组，每个链表都已经按升序排列。 
# 
#  请你将所有链表合并到一个升序链表中，返回合并后的链表。 
# 
#  
# 
#  示例 1： 
# 
#  输入：lists = [[1,4,5],[1,3,4],[2,6]]
# 输出：[1,1,2,3,4,4,5,6]
# 解释：链表数组如下：
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# 将它们合并到一个有序链表中得到。
# 1->1->2->3->4->4->5->6
#  
# 
#  示例 2： 
# 
#  输入：lists = []
# 输出：[]
#  
# 
#  示例 3： 
# 
#  输入：lists = [[]]
# 输出：[]
#  
# 
#  
# 
#  提示： 
# 
#  
#  k == lists.length 
#  0 <= k <= 10^4 
#  0 <= lists[i].length <= 500 
#  -10^4 <= lists[i][j] <= 10^4 
#  lists[i] 按 升序 排列 
#  lists[i].length 的总和不超过 10^4 
#  
#  Related Topics 堆 链表 分治算法 
#  👍 899 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoList(self, l1, l2):
        # 递归调用，合并两个list
        # 可以换成lc21的迭代方式
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoList(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoList(l1, l2.next)
            return l2

    def merge(self, lists, left, right):
        # 二分法：两两合并，数量减半，再两两合并
        if left == right:
            return lists[left]
        mid = left + (right - left) // 2
        l1 = self.merge(lists, left, mid)
        l2 = self.merge(lists, mid+1, right)
        return self.mergeTwoList(l1, l2)

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # 方法1：分治：两两合并
        if not lists:
            return
        return self.merge(lists, 0, len(lists)-1)


    def mergeKLists1(self, lists: List[ListNode]) -> ListNode:
        # 方法2：使用优先队列：时间n*log（k），n为总个数，k为链表数
        import heapq
        res = ListNode(0)
        p, head = res, []
        # 把每个链表存进优先队列里
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(head, (lists[i].val, i))
                lists[i] = lists[i].next

        while head:
            # 弹出一个最外的val节点，并建立节点
            val, index = heapq.heappop(head)
            p.next = ListNode(val)
            p = p.next
            if lists[index]:
                heapq.heappush(head, (lists[index].val, index))
                lists[index] = lists[index].next
        return res.next




