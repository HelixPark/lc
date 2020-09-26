# 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。 
# 
#  示例： 
# 
#  给定一个链表: 1->2->3->4->5, 和 n = 2.
# 
# 当删除了倒数第二个节点后，链表变为 1->2->3->5.
#  
# 
#  说明： 
# 
#  给定的 n 保证是有效的。 
# 
#  进阶： 
# 
#  你能尝试使用一趟扫描实现吗？ 
#  Related Topics 链表 双指针 
#  👍 995 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd1(self, head: ListNode, n: int) -> ListNode:
        # 方式1：两次遍历，第一次获取长度l，第二步找l-n+1
        # 设置个哑结点,指向头，防止只有一个节点的情况
        dummy = ListNode(0)
        dummy.next = head

        cur, size = head, 0
        while cur:
            size += 1
            cur = cur.next

        cur = dummy
        for _ in range(size-n):
            cur = cur.next
        # 删除
        cur.next = cur.next.next
        return dummy.next
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 方式2：一次遍历，快慢指针
        dummy = ListNode(0)
        dummy.next = head
        slow, fast = dummy, dummy
        # fast先走n步
        for _ in range(n):
            fast = fast.next
        # 再同时走,fast达到尾巴，slow指的就是要删除的前一个节点
        while fast and fast.next:
            slow, fast = slow.next, fast.next

        slow.next = slow.next.next
        return dummy.next
    def removeNthFromEnd2(self, head: ListNode, n: int) -> ListNode:
        # 方式3：迭代回溯，进行节点计数
        if not head:
            self.count = 0
            return head
        head.next = self.removeNthFromEnd2(head.next, n)
        self.count += 1  #回溯时进行节点计数
        if self.count == n:
            return head.next
        else:
            return head
