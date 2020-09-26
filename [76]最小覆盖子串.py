
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        start, minLen = 0, float('inf')
        left, right = 0, 0

        window, needs = {}, {}

        # 先把目标t放入hash,key是char，vaule是计数
        for i in range(len(t)):
            if t[i] not in needs:
                needs[t[i]] = 1
            else:
                needs[t[i]] += 1

        match = 0   #就是为了多重复不算，计数一致
        l = len(s)

        while right < l:
            c1 = s[right]
            # right指针定位的元素在needs检查是否存在,存在的话更新两个hash
            if c1 in needs:
                if c1 not in window:
                    window[c1] = 1
                else:
                    window[c1] += 1
                if window[c1] == needs[c1]:
                    match += 1
            right += 1

            # 先走right，mathc匹配完在走left，缩小窗口
            while match == len(needs):
                if (right - left) < minLen:
                    # 更新最小子串位置和长度
                    start = left
                    minLen = right - left

                c2 = s[left]
                if c2 in needs:
                    window[c2] -= 1
                    if window[c2] < needs[c2]:
                        match -= 1
                left += 1

        return '' if minLen == float('inf') else s[start:start+minLen]


S = "ADOBECODEBANC"
T = "ABC"
c = Solution()
# print(c.minWindow(S, T))