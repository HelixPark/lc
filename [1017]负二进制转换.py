# 给出数字 N，返回由若干 "0" 和 "1"组成的字符串，该字符串为 N 的负二进制（base -2）表示。 
# 
#  除非字符串就是 "0"，否则返回的字符串中不能含有前导零。 
# 
#  
# 
#  示例 1： 
# 
#  输入：2
# 输出："110"
# 解释：(-2) ^ 2 + (-2) ^ 1 = 2
#  
# 
#  示例 2： 
# 
#  输入：3
# 输出："111"
# 解释：(-2) ^ 2 + (-2) ^ 1 + (-2) ^ 0 = 3
#  
# 
#  示例 3： 
# 
#  输入：4
# 输出："100"
# 解释：(-2) ^ 2 = 4
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= N <= 10^9 
#  
#  Related Topics 数学 
#  👍 30 👎 0


class Solution:
    def baseNeg2(self, N: int) -> str:
        # 被除数除以 - 2,如果"余"为负数的情况则需要重新计算"商"值;
        # 如：3 // -2 = -2(商), 3 % -2 = -1(余);
        # 余数置正后对应表达式为 - 2 * -1(商) + 1(余) = 3;
        # 此时计算下一步的被除数从 - 2变成了 - 1, 这是关键;
        if N == 0:return '0'

        beichushu, res = N, []
        while beichushu != 0:
            yushu = beichushu % -2
            if yushu < 0:
                yushu = 1
                beichushu = (beichushu - yushu) // -2
            else:
                beichushu = beichushu // -2
            res.append(str(yushu))
        res.reverse()
        return ''.join(res)
