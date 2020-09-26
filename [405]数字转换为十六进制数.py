# 给定一个整数，编写一个算法将这个数转换为十六进制数。对于负整数，我们通常使用 补码运算 方法。 
# 
#  注意: 
# 
#  
#  十六进制中所有字母(a-f)都必须是小写。 
#  十六进制字符串中不能包含多余的前导零。如果要转化的数为0，那么以单个字符'0'来表示；对于其他情况，十六进制字符串中的第一个字符将不会是0字符。 
#  给定的数确保在32位有符号整数范围内。 
#  不能使用任何由库提供的将数字直接转换或格式化为十六进制的方法。 
#  
# 
#  示例 1： 
# 
#  
# 输入:
# 26
# 
# 输出:
# "1a"
#  
# 
#  示例 2： 
# 
#  
# 输入:
# -1
# 
# 输出:
# "ffffffff"
#  
#  Related Topics 位运算 
#  👍 92 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def toHex(self, num: int) -> str:
        # 核心思想，使用位运算，每4位，对应1位16进制数字
        # 使用0xf(0..01111b)获取num的低4位。
        # >>算数位移，正数右移左边补0，负数右移左边补1
        if num == 0:
            return "0"
        hex= "0123456789abcdef"  #相当于映射关系
        res = ''
        # 位运算不能保证num为0，所以要32位对应8位长度来保证
        while num and len(res) <8:
            tmp = num & 0xf #取低4位的十进制
            t = hex[tmp]    #映射对应16进制字符
            res = t+res #放在前面
            # res = hex[num&0xf]+res
            num >>= 4   #逻辑右移4位
        return res
num = -1
c = Solution()
print(c.toHex(num))
