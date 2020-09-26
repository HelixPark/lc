# 给定一组非负整数，重新排列它们的顺序使之组成一个最大的整数。 
# 
#  示例 1: 
# 
#  输入: [10,2]
# 输出: 210 
# 
#  示例 2: 
# 
#  输入: [3,30,34,5,9]
# 输出: 9534330 
# 
#  说明: 输出结果可能非常大，所以你需要返回一个字符串而不是整数。 
#  Related Topics 排序 
#  👍 386 👎 0

class LargeNumKey(str):
    # 传递性
    def __lt__(x,y):
        return x+y > y+x

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # 为了构建最大数字，希望每项越高位的数字越大越好。
        # 重载比较运算符lt(less than)。将数组中所有元素类型改为字符串
        # 对数组排序（降序），key为重载后的lt
        # 将排序后的数组拼接起来输出
        # 如果第一个元素就为 ‘0’，说明所有元素均为 ‘0’，则返回 ‘0’
        largeNum = ''.join(sorted(map(str,nums),key=LargeNumKey))
        if largeNum[0] == '0':
            return '0'
        else:
            return largeNum
