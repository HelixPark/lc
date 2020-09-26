# 给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。 
# 
#  示例 1: 
# 
#  输入: 1->1->2
# 输出: 1->2
#  
# 
#  示例 2: 
# 
#  输入: 1->1->2->3->3
# 输出: 1->2->3 
#  Related Topics 链表 
#  👍 396 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # 直接法
        cur = head
        while cur != None and cur.next != None:
            if cur.next.val == cur.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head