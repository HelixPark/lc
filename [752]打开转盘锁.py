
# utf-8
from typing import List
class Solution:
    # s[i]向上拨动
    def plusOne(self,s:str,i:int):
        s = list(s)
        if s[i] == '9':
            s[i] = '0'
        else:
            s[i] = str(int(s[i]) + 1)
        return ''.join(s)

    # s[i]向下拨动
    def minusOne(self,s:str,i:int):
        s = list(s)
        if s[i] == '0':
            s[i] = '9'
        else:
            s[i] = str(int(s[i]) - 1)
        return ''.join(s)

    def openLock1(self, deadends: List[str], target: str) -> int:
        # 单向BFS
        # visited防止走回头路
        deadHashSet, visitedHashSet = set(), set()
        # 把跳过的dead放进set
        for d in deadends:
            deadHashSet.add(d)

        queue = []
        queue.append('0000')
        visitedHashSet.add('0000')
        count = 0

        while len(queue) != 0:
            sz = len(queue)
            # 将当前队列中的所有节点向周围扩散
            for i in range(sz):
                cur = queue.pop(0)

                # 判断是否终点
                if cur in deadHashSet:
                    continue
                if cur == target:
                    return count

                # 将这个节点周边8个节点加入队列
                for j in range(4):

                    plus = self.plusOne(cur,j)
                    # 若未遍历过，则加入队列
                    if plus not in visitedHashSet:
                        queue.append(plus)
                        visitedHashSet.add(plus)

                    minus = self.minusOne(cur,j)
                    if minus not in visitedHashSet:
                        queue.append(minus)
                        visitedHashSet.add(minus)
            count += 1
        return -1

    def openLock(self, deadends: List[str], target: str) -> int:
        # 双向BFS：前提需要知道target，用hash而不用队列
        # visited防止走回头路
        deadHashSet, visitedHashSet = set(), set()
        # 把跳过的dead放进set
        for d in deadends:
            deadHashSet.add(d)

        q1, q2 = set(), set()
        q1.add('0000')
        q2.add(target)
        count = 0

        while len(q1) != 0 and len(q2) != 0:
            # 哈希集合在遍历的过程中不能修改，⽤temp存储扩散结果
            tmp = set()
            # 将q1中的所有节点向周围扩散
            for cur in q1:
                if cur in deadHashSet:
                    continue
                if cur in q2:
                    return count
                visitedHashSet.add(cur)

                # 将⼀个节点的未遍历相邻节点加⼊集合
                for j in range(4):
                    plus = self.plusOne(cur, j)
                    if plus not in visitedHashSet:
                        tmp.add(plus)
                    minus = self.minusOne(cur, j)
                    if minus not in visitedHashSet:
                        tmp.add(minus)
            count += 1
            # temp相当于q1,交换q1,q2
            q1 = q2
            q2 = tmp
        return -1

deadends = ["0201","0101","0102","1212","2002"]
target = "0202"
c = Solution()
print(c.openLock(deadends,target))