# 给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。 
# 
#  示例 1: 
# 
#  输入: 1->2->3->3->4->4->5
# 输出: 1->2->5
#  
# 
#  示例 2: 
# 
#  输入: 1->1->1->2->3
# 输出: 2->3 
#  Related Topics 链表 
#  👍 370 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates1(self, head: ListNode) -> ListNode:
        # 简单解法：一次遍历
        # 首先构建一个虚拟头结点, 防止头结点这里是重复结点
        dummy = ListNode(0)
        dummy.next = head
        pre, cur = dummy, head

        while cur != None and cur.next != None:
            # 元素重复
            if cur.val == cur.next.val:
                tmp = cur.val
                cur = cur.next.next
                while cur != None and cur.val == tmp:
                    cur = cur.next
                pre.next = cur
            else:
                pre = cur
                cur = cur.next
        return dummy.next
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # 递归:删除所有头部的重复节点，返回不重复的第一个节点。
        if head == None or head.next == None:
            return head
        if head.val == head.next.val:
            while head != None and head.next != None \
                    and head.val == head.next.val:
                head = head.next
            return self.deleteDuplicates(head.next)
        else:
            head.next = self.deleteDuplicates(head.next)
            return head