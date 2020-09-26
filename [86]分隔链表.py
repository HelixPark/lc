# 给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。 
# 
#  你应当保留两个分区中每个节点的初始相对位置。 
# 
#  
# 
#  示例: 
# 
#  输入: head = 1->4->3->2->5->2, x = 3
# 输出: 1->2->2->4->3->5
#  
#  Related Topics 链表 双指针 
#  👍 257 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        # 链表头都初始化为哑节点，组合和返回时注意后移一个
        former = formerHead = ListNode(0)
        latter = latterHead = ListNode(0)

        while head:
            if head.val < x:
                # 若小于x，这个节点应该属于former，否则
                former.next = head
                former = former.next
            else:
                latter.next = head
                latter = latter.next

            head = head.next
        # 形成了两个链表，再组合一块儿
        latter.next = None
        former.next = latterHead.next
        return formerHead.next