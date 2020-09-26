# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        head = ListNode(0)   #新建链表头，存储结果
        r = head
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            s = carry + x + y
            carry = s // 10

            r.next = ListNode(s%10)
            r = r.next

            if l1 != None:
                l1 = l1.next
            if l2 != None:
                l2 = l2.next
        # 看最后（最高位）有没有进位
        if carry > 0:
            r.next = ListNode(1)
        return head.next

