
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # 双指针法:回溯。用while架构
        # 移动txt上的p1指针，直到p1所指向位置的字符与pattern字符串第一个字符相等。
        # 通过 p1，p2，curr_len 计算匹配长度。
        # 如果完全匹配（即 curr_len == len_pat），返回匹配子串的起始坐标（即 p1 - len_pat）。
        # 如果不完全匹配，回溯。使 p1 = p1 - curr_len + 1， p2 = 0， curr_len = 0。
        pattern, txt = needle, haystack
        len_pattern, len_txt = len(pattern), len(txt)

        if len_pattern == 0:
            return 0
        # p1是用在txt上的指针，p2是用在pattern 的指针
        p1 = 0
        while p1 < len_txt - len_pattern + 1:
            # txt中移动p1，找与pat第一个位置比较,不相等就后移
            while p1 < len_txt - len_pattern + 1 and txt[p1] != pattern[0]:
                p1 += 1

            # 首字符相等后，计算最长匹配长度
            cur_len, p2 = 0, 0
            while p2 < len_pattern and p1 < len_txt and txt[p1] == pattern[p2]:
                p1 += 1
                p2 += 1
                cur_len += 1

            # 完全匹配
            if cur_len == len_pattern:
                return p1 - len_pattern

            # 不完全匹配就回溯
            p1 = p1 - cur_len + 1

        return -1


    def strStr2(self, haystack: str, needle: str) -> int:
        # kmp算法用空间换时间，存储信息
        class KMP:
            def __init__(self, pattern):
                self.pattern = pattern
                # 256代表ascii数量，初始为0,创建DP数组(传值中介)
                self.dp = [[0] * 256 for _ in range(len(self.pattern))]

            # 通过pattern构建dp数组。需要o(n)
            def KMP_Function(self):
                len_pattern = len(self.pattern)

                # base case
                self.dp[0][ord(self.pattern[0])] = 1
                # 影子状态初始为0
                X = 0
                # 构建状态转移图
                for j in range(len_pattern):
                    for c in range(256):
                        self.dp[j][c] = self.dp[X][c]
                    self.dp[j][ord(self.pattern[j])] = j + 1

                    # 更新影子状态
                    X = self.dp[X][ord(self.pattern[j])]

            # 通过已保存的dp数组去匹配txt，需要o(N)
            def Search_Function(self, txt: str):
                len_pattern, len_text = len(self.pattern), len(txt)

                # pattern的初始状态j为0
                j = 0
                for i in range(len_text):
                    # 当前状态为j，遇到txt[i]
                    # ord()根据字符转对应的ASCII值
                    j = self.dp[j][ord(txt[i])]

                    # 如果达到终止态，返回匹配索引的开头
                    if j == len_pattern:
                        return i - len_pattern + 1
                # 没有达到终止态，匹配失败
                return -1

        kmp = KMP(needle)
        kmp.KMP_Function()
        return kmp.Search_Function(haystack)
