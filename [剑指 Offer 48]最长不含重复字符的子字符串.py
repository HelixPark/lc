# 请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。 
# 
#  
# 
#  示例 1: 
# 
#  输入: "abcabcbb"
# 输出: 3 
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
#  
# 
#  示例 2: 
# 
#  输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
#  
# 
#  示例 3: 
# 
#  输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
#  
# 
#  
# 
#  提示： 
# 
#  
#  s.length <= 40000 
#  
# 
#  注意：本题与主站 3 题相同：https://leetcode-cn.com/problems/longest-substring-without-rep
# eating-characters/ 
#  Related Topics 哈希表 双指针 Sliding Window 
#  👍 89 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 双指针和滑动窗口
        left, right = 0, 0
        window = {}
        res = 0

        while right < len(s):
            # right先走
            c1 = s[right]

            if c1 not in window:
                window[c1] = 1
            else:
                window[c1] += 1

            right += 1

            # 如果滑动窗口中出现重复字符，开始缩小窗口，left后移
            while window[c1] > 1:
                c2 = s[left]
                window[c2] -= 1
                left += 1
            res = max(res, right - left)
        return res