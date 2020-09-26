# 给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。 
# 
#  k 是一个正整数，它的值小于或等于链表的长度。 
# 
#  如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。 
# 
#  
# 
#  示例： 
# 
#  给你这个链表：1->2->3->4->5 
# 
#  当 k = 2 时，应当返回: 2->1->4->3->5 
# 
#  当 k = 3 时，应当返回: 3->2->1->4->5 
# 
#  
# 
#  说明： 
# 
#  
#  你的算法只能使用常数的额外空间。 
#  你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。 
#  
#  Related Topics 链表 
#  👍 738 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # 迭代：反转 k 个元素，然后一直执行这个操作。
        # 反转前要考虑剩余元素的个数（小于k不需要反转），看是否需要反转

        # 反转 k 个元素，返回反转后的头、尾节点。
        def revrese(head, k):
            pre, cur = None, head
            for _ in range(k):
                cur.next, pre, cur = pre, cur, cur.next
            return pre, head

        pre = res = ListNode(0)
        res.next = head

        while pre.next:
            # 判断剩余节点个数是否有 k 个，若没有直接返回。
            # 另一个目的是将 cur 定位到 k+1 个节点的位置，方便后续的拼接。
            cur = pre.next
            for _ in range(k):
                if not cur:
                    return res.next
                cur = cur.next

            pre.next, pre = revrese(pre.next, k)  # 将 pre 连接已经反转好的元素，顺便移动 pre 的位置。
            pre.next = cur  # 拼接剩余元素，否则无法继续迭代。
        return res.next
