

class Solution:
    def reverseList1(self, head: ListNode) -> ListNode:
        # 递归解法，参考见微信收藏
        # https://mp.weixin.qq.com/s/yPFGK1SM8yNbw6cE0zHTXA
        if head == None or head.next == None:
            return head

        newNode = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return newNode

    def reverseList2(self, head: ListNode) -> ListNode:
        # 原地反转，双指针，迭代
        # 参考https://mp.weixin.qq.com/s/yPFGK1SM8yNbw6cE0zHTXA
        prev, curr = None, head

        while curr != None:
            nxt = curr.next
            curr.next = prev    #翻转箭头
            prev = curr   #同步后移
            curr = nxt      #同步后移
        return prev
    def reverseList(self, head: ListNode) -> ListNode:
        # 头插法:
        if head == None or head.next == None:
            return head

        # 操作头节点, 2次指针操作,头节点head.next赋值给cur,
        # 由于头节点最终要成为尾结点, 其指向为空
        cur = head.next  #head.next赋值给cur
        head.next = None

        # 然后把每一个cur插入到head
        while cur != None:
            nxt = cur.next  #nxt为cur后面的节点
            cur.next = head  #cur.next指向head

            head = cur  #指定头节点

            cur = nxt   #移动cur
        return head
