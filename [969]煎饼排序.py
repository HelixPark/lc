from typing import List
# utf-8
class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        res = []

        def reverse(arr, i, j):
            while i < j:
                tmp = arr[i]
                arr[i] = arr[j]
                arr[j] = tmp
                i += 1
                j -= 1
        
        def go_sort(cakes, n):
            # base case
            if n == 1: return

            # ps：数组index从0开始，要返回的数要从1开始，
            # 寻找最大饼的索引
            maxCake, maxCakeIndex = 0, 0
            for i in range(n):
                if cakes[i] > maxCake:
                    maxCakeIndex = i
                    maxCake = cakes[i]

            # 第一次翻转,将最大的饼翻到上面
            reverse(cakes, 0 ,maxCakeIndex)
            res.append(maxCakeIndex + 1)
            # 第二次翻转,将最大的饼翻到下面
            reverse(cakes, 0, n-1)
            res.append(n)
            # 递归调用
            go_sort(cakes,n-1)

        go_sort(cakes=A,n=len(A))
        return res

# a = [3,2,4,1]
a = [1,2,3]
c = Solution()
print(c.pancakeSort(a))