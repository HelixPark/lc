# 给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。 
# 
#  
# 
#  提示： 
# 
#  
#  num1 和num2 的长度都小于 5100 
#  num1 和num2 都只包含数字 0-9 
#  num1 和num2 都不包含任何前导零 
#  你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式 
#  
#  Related Topics 字符串 
#  👍 260 👎 0


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # 双指针，均指向尾部，模拟加法
        res = ""
        i, j, carry = len(num1) - 1, len(num2) - 1, 0
        while i >= 0 or j >= 0:
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0
            tmp = n1 + n2 + carry
            carry = tmp // 10
            res = str(tmp % 10) + res
            i, j = i - 1, j - 1
        return "1" + res if carry else res
