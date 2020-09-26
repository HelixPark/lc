from typing import List
class Solution:
    def findAnagrams1(self, s: str, p: str) -> List[int]:
        # 单指针：sorted占用，超时
        l_s, l_p = len(s), len(p)
        res = []

        for i in range(l_s - l_p + 1):
            if sorted(s[i:i+l_p]) == sorted(p):
                res.append(i)
        return res

    def findAnagrams(self, s: str, p: str) -> List[int]:
        # 双指针:滑动窗口
        res = []
        left, right = 0, 0
        windows, needs = {}, {}
        match = 0


        # 先把目标p放入hash,key是char，vaule是计数
        for i in range(len(p)):
            if p[i] not in needs:
                needs[p[i]] = 1
            else:
                needs[p[i]] += 1

        while right < len(s):
            c1 = s[right]
            # c1在needs里面就进去，否则直接后移
            if c1 in needs:
                if c1 not in windows:
                    windows[c1] = 1
                else:
                    windows[c1] += 1
                if windows[c1] == needs[c1]:
                    match += 1
            right += 1

            # 如果连续匹配数（窗口大小）合适，则left加入res索引
            while match == len(needs):
                if right - left == len(p):
                    res.append(left)

                c2 = s[left]
                if c2 in needs:
                    windows[c2] -= 1
                    if windows[c2] < needs[c2]:
                        match -= 1
                left += 1
        return res



