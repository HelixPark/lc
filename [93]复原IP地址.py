# 给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。 
# 
#  有效的 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。 
# 
#  例如："0.1.2.201" 和 "192.168.1.1" 是 有效的 IP 地址，但是 "0.011.255.245"、"192.168.1.312"
#  和 "192.168@1.1" 是 无效的 IP 地址。 
# 
#  
# 
#  示例 1： 
# 
#  输入：s = "25525511135"
# 输出：["255.255.11.135","255.255.111.35"]
#  
# 
#  示例 2： 
# 
#  输入：s = "0000"
# 输出：["0.0.0.0"]
#  
# 
#  示例 3： 
# 
#  输入：s = "1111"
# 输出：["1.1.1.1"]
#  
# 
#  示例 4： 
# 
#  输入：s = "010010"
# 输出：["0.10.0.10","0.100.1.0"]
#  
# 
#  示例 5： 
# 
#  输入：s = "101023"
# 输出：["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= s.length <= 3000 
#  s 仅由数字组成 
#  
#  Related Topics 字符串 回溯算法 
#  👍 423 👎 0


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # 递归DFS：定义查找符合条件的数字个数
        NUM = 4
        def dfs(start, path):
            # 结束条件
            if len(path) > NUM or (len(path) == NUM and start < len(s) - 1):
                return
            # 追加结果
            if start >= len(s):
                if len(path) == NUM:
                    res.append('.'.join(path))
                return

            # 当前是0, 特殊情况处理
            if s[start] == '0':
                path.append(s[start])
                dfs(start + 1, path)
                path.pop()
                return
            # 递归查找
            for i in range(start, len(s)):
                if 0 <= int(s[start:i + 1]) <= 255:
                    path.append(s[start:i + 1])
                    dfs(i + 1, path)
                    path.pop()
                else:
                    break
            return
        res = []
        dfs(0, [])
        return res