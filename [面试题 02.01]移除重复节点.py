
class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        # 利用哈希表，依次遍历每一个节点，
        # 如果这个节点的值不在于哈希表中，将该节点的值添加到哈希表中，
        # 否则将该节点删除
        if head == None or head.next == None:
            return head

        # 头结点指定放进hashset，不重复
        hashTable = set()
        hashTable.add(head.val)

        pre_node, cur_node = head, head.next

        while cur_node:
            tmp = cur_node.next
            # cur_node不在hash里面，添加进去，依次后移
            if cur_node.val not in hashTable:
                hashTable.add(cur_node.val)
                pre_node = cur_node

            else:
                # 在hash里面，则删除此节点
                pre_node.next = cur_node.next
                del cur_node
            cur_node = tmp
        return head