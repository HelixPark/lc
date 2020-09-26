# 输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。 
# 
#  
# 
#  示例 1： 
# 
#  输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]
#  
# 
#  示例 2： 
# 
#  输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 输出：[1,2,3,4,8,12,11,10,9,5,6,7]
#  
# 
#  
# 
#  限制： 
# 
#  
#  0 <= matrix.length <= 100 
#  0 <= matrix[i].length <= 100 
#  
# 
#  注意：本题与主站 54 题相同：https://leetcode-cn.com/problems/spiral-matrix/ 
#  Related Topics 数组 
#  👍 132 👎 0

from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        rows, columns = len(matrix), len(matrix[0])
        res = []
        left, right, top, bottom = 0, columns-1, 0 ,rows-1
        while left <= right and top <= bottom:
            # 从左向右打
            for col in range(left, right+1):
                res.append(matrix[top][col])
            # 从上到下打
            for row in range(top+1,bottom+1):
                res.append(matrix[row][right])

            if left < right and top < bottom:
                # 底层：从右向左打
                for col in range(right-1,left,-1):
                    res.append(matrix[bottom][col])
                for row in range(bottom,top,-1):
                    res.append(matrix[row][left])
            # 四个角收缩
            left, right, top, bottom = left+1, right-1, top+1, bottom-1
        return res

matrix = [[1, 2, 3, 4, 5, 6, 7],
 [1, 2, 3, 4, 5, 6, 7],
 [1, 2, 3, 4, 5, 6, 7],
 [1, 2, 3, 4, 5, 6, 7],
 [1, 2, 3, 4, 5, 6, 7]]

c = Solution()
c.spiralOrder(matrix)