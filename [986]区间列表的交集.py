from typing import List
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        res = []

        while i < len(A) and j < len(B):
            a1, a2 = A[i][0], A[i][1]
            b1, b2 = B[j][0], B[j][1]

            # 不存在交集的为b1 > a2 or a1 >b2,否命题就是存在交集
            # 如果两个区间存在交集
            if b2 >= a1 and a2 >= b1:
                # 计算交集
                res.append([max(a1,b1),min(a2,b2)])
            # 指针前进:是否前进，只取决于a2 b2
            if b2 < a2:
                j += 1
            else:
                i += 1
        return res

A = [[0,2],[5,10],[13,23],[24,25]]
B = [[1,5],[8,12],[15,24],[25,26]]
c = Solution()
c.intervalIntersection(A,B)