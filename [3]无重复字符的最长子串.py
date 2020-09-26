


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

s = "abcabcbb"
c = Solution()
c.lengthOfLongestSubstring(s)