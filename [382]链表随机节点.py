# 给定一个单链表，随机选择链表的一个节点，并返回相应的节点值。保证每个节点被选的概率一样。 
# 
#  进阶: 
# 如果链表十分大且长度未知，如何解决这个问题？你能否使用常数级空间复杂度实现？ 
# 
#  示例: 
# 
#  
# // 初始化一个单链表 [1,2,3].
# ListNode head = new ListNode(1);
# head.next = new ListNode(2);
# head.next.next = new ListNode(3);
# Solution solution = new Solution(head);
# 
# // getRandom()方法应随机返回1,2,3中的一个，保证每个元素被返回的概率相等。
# solution.getRandom();
#  
#  Related Topics 蓄水池抽样 
#  👍 66 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import random
class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head
        

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        import random
        i, res = 0, 0
        cur = self.head
        while cur != None:
            i += 1
            # 效果一样:这个生成的整数等于谁不重要，主要代表了每个数的概率一样==i or ==1
            # if random.randrange(i) == 0:
            # 生成一个[1，i]之间的整数（均闭区间），这个整数等于1的概率就是1/i
            # if random.randint(1,i) == i:
            # 极端考虑：如果只有一个，第一次i为1，产生的随机数也只有1，概率唯一，且等概率
            if random.randint(1,i) == 1:
                res = cur.val
            cur = cur.next
        return res


    def getRandom_K(self):
        # 返回链表中k个随机节点的值：使每个概率一致
        import random
        res = []
        cur = self.head
        K = 3
        # 前k个元素默认先选上.默认链表长度大于K
        for i in range(K):
            res.append(cur.val)
            cur = cur.next

        i = K
        while cur != None:
            i += 1
            generate = random.randint(1,i)
            # 这个整数小于k的概率就是k / i
            if generate < K:
                res[generate - 1] = cur.val
            cur = cur.next

        return res

    def listRandom(self,nums):
        # 针对数组的
        # 水塘抽样，数组，等概率
        n, res = len(nums), 0
        for i in range(n):
            if random.randint(0,i+1) == 0:
                res = nums[i]
        return res

    def listRandomK(self,nums, K):
        # 随机选择k个数，
        # 只要在第i个元素处以k / i的概率选择该元素，
        # 以1 - k / i的概率保持原有选择
        n, res = len(nums), []

        # 前k个默认先选上
        for i in range(n):
            if i < K:
                # 先把前k个放进去
                res.append(nums[i])
            else:
                # 生成一个数，如果这个小于K，就替换数组
                generate = random.randint(0,i)
                if generate < K:
                    res[generate] = nums[i]
        return res






# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
# leetcode submit region end(Prohibit modification and deletion)
