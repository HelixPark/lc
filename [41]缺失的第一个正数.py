
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        print('d')
        # 若没有额外的时空复杂度要求，那么就很容易实现：
        # 1.可以将数组所有的数放入哈希表，随后从1开始依次枚举正整数，并判断其是否在哈希表中；
        # 2.可以从开始依次枚举正整数，并遍历数组，判断其是否在数组中。
        # 如果数组的长度为N，那么第一种做法的时间复杂度为O(N)，空间复杂度为O(N)；
        # 第二种做法的时间复杂度为O(N ^ 2)，空间复杂度为O(1)。但它们都不满足题目的要求：时间复杂度为O(N)，空间复杂度为O(1)。

        # 「真正」满足此要求的算法是不存在的。
        # 但是我们可以退而求其次：利用给定数组中的空间来存储一些状态。
        # 也就是说，如果题目给定的数组是不可修改的，那么就不存在满足时空复杂度要求的算法；
        # 但如果我们可以修改给定的数组，那么是存在满足要求的算法的
        # 只能使用常数级别的额外空间，在这个限制下本题的思路有一个非正式的名称：原地哈希


        n = len(nums)
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1

        for i in range(n):
            num = abs(nums[i])
            if num <= n:
                nums[num-1] = -abs(nums[num-1])

        for i in range(n):
            if nums[i] > 0:
                return i + 1
        return n+1