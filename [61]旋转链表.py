# 给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。 
# 
#  示例 1: 
# 
#  输入: 1->2->3->4->5->NULL, k = 2
# 输出: 4->5->1->2->3->NULL
# 解释:
# 向右旋转 1 步: 5->1->2->3->4->NULL
# 向右旋转 2 步: 4->5->1->2->3->NULL
#  
# 
#  示例 2: 
# 
#  输入: 0->1->2->NULL, k = 4
# 输出: 2->0->1->NULL
# 解释:
# 向右旋转 1 步: 2->0->1->NULL
# 向右旋转 2 步: 1->2->0->NULL
# 向右旋转 3 步: 0->1->2->NULL
# 向右旋转 4 步: 2->0->1->NULL 
#  Related Topics 链表 双指针 
#  👍 300 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # 先闭环，在相应位置断开这个环，确定新链表的投和尾巴
        if not head:
            return None
        if not head.next:
            return head

        # 闭环
        old_tail = head
        count = 1
        while old_tail.next:
            old_tail = old_tail.next
            count += 1
        old_tail.next = head

        # 找新头和新尾巴
        new_tail = head
        for i in range(count- k % count -1):
            new_tail = new_tail.next
        new_head = new_tail.next

        # 断开
        new_tail.next = None
        return new_head