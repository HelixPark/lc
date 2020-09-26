# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。 
# 
#  有效字符串需满足： 
# 
#  
#  左括号必须用相同类型的右括号闭合。 
#  左括号必须以正确的顺序闭合。 
#  
# 
#  注意空字符串可被认为是有效字符串。 
# 
#  示例 1: 
# 
#  输入: "()"
# 输出: true
#  
# 
#  示例 2: 
# 
#  输入: "()[]{}"
# 输出: true
#  
# 
#  示例 3: 
# 
#  输入: "(]"
# 输出: false
#  
# 
#  示例 4: 
# 
#  输入: "([)]"
# 输出: false
#  
# 
#  示例 5: 
# 
#  输入: "{[]}"
# 输出: true 
#  Related Topics 栈 字符串 
#  👍 1695 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict = {')':'(', ']':'[', '}':'{'}

        for i in s:
            # 如果是左括号，入栈
            if i not in dict:
                stack.append(i)
            else:
                # 是右括号
                # 右括号对应的元素和栈顶的元素是否匹配，bu匹配直接false
                if len(stack) != 0 and stack.pop() == dict[i]:
                    continue
                else:
                    return False
        # 遍历一遍后，stack为空就说明完全匹配，返回True
        return not stack

s = ']'
c = Solution()
print(c.isValid(s))