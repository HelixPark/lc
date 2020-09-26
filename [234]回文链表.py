# 请判断一个链表是否为回文链表。 
# 
#  示例 1: 
# 
#  输入: 1->2
# 输出: false 
# 
#  示例 2: 
# 
#  输入: 1->2->2->1
# 输出: true
#  
# 
#  进阶： 
# 你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？ 
#  Related Topics 链表 双指针 
#  👍 564 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome2(self, head: ListNode) -> bool:
        # 借助⼆叉树后序遍历的思路，不需要显式反转原始链表也可以倒序遍历链表
        # 打印放在递归traver之后，right指针先到尾结点，实际效果就是倒序打印
        self.left = head

        def traverse(right: ListNode):

            if right == None:
                return True

            res = traverse(right.next)
            # 后序遍历
            res = res & (right.val == self.left.val)
            self.left = self.left.next
            return res
        return traverse(head)

    def find_end_of_former(self,head):
        # 使用快慢指针找到前半部分的尾结点，
        # 若是奇数，中间的算前半部分
        fast, slow = head, head
        while fast.next != None and fast.next.next != None:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse_list(self,head):
        # 插入法逆序
        pre, cur = None, head
        while cur != None:
            next_node = cur.next
            cur.next = pre

            pre = cur
            cur = next_node
        return pre

    def isPalindrome(self, head: ListNode) -> bool:
        if head == None:
            return True

        end_of_former = self.find_end_of_former(head)
        start_of_last = self.reverse_list(end_of_former.next)

        # 检查是否回文
        res = True
        pos_1, pos_2 = head, start_of_last
        while res and pos_2 is not None:
            if pos_1.val != pos_2.val:
                res = False
            pos_1, pos_2 = pos_1.next, pos_2.next

        # 回复链表
        end_of_former.next = self.reverse_list(start_of_last)
        return res