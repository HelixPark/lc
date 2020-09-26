# 给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，在字符串中增加空格来构建一个句子，使得句子中所有的单词都在词典中。返回所有这些可能的
# 句子。 
# 
#  说明： 
# 
#  
#  分隔时可以重复使用字典中的单词。 
#  你可以假设字典中没有重复的单词。 
#  
# 
#  示例 1： 
# 
#  输入:
# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]
# 输出:
# [
#   "cats and dog",
#   "cat sand dog"
# ]
#  
# 
#  示例 2： 
# 
#  输入:
# s = "pineapplepenapple"
# wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
# 输出:
# [
#   "pine apple pen apple",
#   "pineapple pen apple",
#   "pine applepen apple"
# ]
# 解释: 注意你可以重复使用字典中的单词。
#  
# 
#  示例 3： 
# 
#  输入:
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
# 输出:
# []
#  
#  Related Topics 动态规划 回溯算法 
#  👍 236 👎 0


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # 方式1：动态规划
        tmp = set("".join(wordDict))
        if any([i not in tmp for i in s]):
            return []
        # dp[i] 表示s中前i个字符的划分结果，以list的形式存储。
        dp = [[""], [s[0]] * (s[0] in wordDict)]
        tmp = []
        for i in range(1, len(s)):
            for j in range(i + 1):
                if dp[j] and s[j:i + 1] in wordDict:
                    for k in dp[j]:
                        if k:
                            tmp.append([f"{k} {s[j:i + 1]}"])
                        else:
                            tmp.append([s[j:i + 1]])
            dp.append(sum(tmp, []))
            tmp = []
        return dp[-1]

    def wordBreak1(self, s: str, wordDict: List[str]) -> List[str]:
        # 方式2：dfs
        return self.dfs(s, wordDict, {})

    def dfs(self, s, wordDict, map):
        if s in map: return map[s]
        if not s: return ['']

        res = []
        for word in wordDict:
            if not s.startswith(word):
                continue
            # 递归解决剩余的部分
            # 每一个item都是一种以word开头可能的拆分方案
            for item in self.dfs(s[len(word):], wordDict, map):
                item = word + ('' if item == '' else ' ') + item
                res.append(item)
        map[s] = res
        return res