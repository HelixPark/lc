
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 这道题目最开始大家想的肯定是sort，然后计数计算最长序列。
        # 但是要求时间复杂度为：o(n)，就不能用sort了。
        # 一般在leetcode中，对时间复杂度有要求，就用空间来换，
        # 对空间复杂度有要求，就用时间来换。

        # 考虑枚举数组中的每个数 x，考虑以其为起点，
        # 不断尝试匹配 x+1,x+2,⋯ 是否存在，
        # 假设最长匹配到了x+y，那么以x为起点的最长连续序列
        # 即为 x,x+1,x+2,⋯,x+y，其长度为y+1，不断枚举并更新答案即可。

        # 对于匹配的过程，暴力的方法是O(n)
        # 遍历数组去看是否存在这个数，但更高效的方法是用一个哈希表存储数组中的数，
        # 这样查看一个数是否存在即能优化至O(1)

        # 仔细分析这个过程，我们会发现其中执行了很多不必要的枚举，如果已知有一个
        # x, x + 1, x + 2,⋯, x + y的连续序列，而我们却重新从x + 1，x + 2或者是x + y
        # 处开始尝试匹配，那么得到的结果肯定不会优于枚举x为起点的答案，
        # 因此我们在外层循环的时候碰到这种情况跳过即可

        # 那么怎么判断是否跳过呢？
        # 由于我们要枚举的数x一定是在数组中不存在前驱数x - 1的，
        # 不然按照上面的分析我们会从x - 1开始尝试匹配，因此我们每次在哈希表中检查是否存在x - 1

        # 未排序的数组求最长连续序列的长度
        longest = 0
        # 去重
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                cur_num = num
                cur_streak =1

                while cur_num + 1 in num_set:
                    cur_num += 1
                    cur_streak += 1
                longest = max(longest,cur_streak)

        return longest

    def longestConsecutive1(self, nums):
        hash_dict = dict()

        max_length = 0
        for num in nums:
            if num not in hash_dict:
                left = hash_dict.get(num - 1, 0)
                right = hash_dict.get(num + 1, 0)

                cur_length = 1 + left + right
                if cur_length > max_length:
                    max_length = cur_length

                hash_dict[num] = cur_length
                hash_dict[num - left] = cur_length
                hash_dict[num + right] = cur_length

        return max_length