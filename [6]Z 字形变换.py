# 将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。 
# 
#  比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下： 
# 
#  L   C   I   R
# E T O E S I I G
# E   D   H   N
#  
# 
#  之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。 
# 
#  请你实现这个将字符串进行指定行数变换的函数： 
# 
#  string convert(string s, int numRows); 
# 
#  示例 1: 
# 
#  输入: s = "LEETCODEISHIRING", numRows = 3
# 输出: "LCIRETOESIIGEDHN"
#  
# 
#  示例 2: 
# 
#  输入: s = "LEETCODEISHIRING", numRows = 4
# 输出: "LDREOEIIECIHNTSG"
# 解释:
# 
# L     D     R
# E   O E   I I
# E C   I H   N
# T     S     G 
#  Related Topics 字符串 
#  👍 842 👎 0


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2: return s
        res = ["" for _ in range(numRows)]
        i, flag = 0, -1
        # 按顺序遍历s，
        for c in s:
            # 把每个字符c填进对应的行，
            res[i] += c
            if i == 0 or i == numRows - 1:
                # 达到z字形转折，执行反向
                flag = -flag
            # 更新当前字符c的行索引
            i += flag
        return "".join(res)
