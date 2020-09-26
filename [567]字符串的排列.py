
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        left, right = 0, 0
        windows, needs = {}, {}
        match = 0

        # 把s1放入hash先
        for i in range(len(s1)):
            if s1[i] not in needs:
                needs[s1[i]] = 1
            else:
                needs[s1[i]] += 1

        # 移动指针
        while right < len(s2):

            c1 = s2[right]
            if c1 in needs:
                if c1 not in windows:
                    windows[c1] = 1
                else:
                    windows[c1] += 1

                if windows[c1] == needs[c1]:
                    match += 1

            right += 1

            # 如果匹配合适，返回true
            while right - left >= len(s1):
                if match == len(needs):
                    return True

                c2 = s2[left]
                if needs.get(c2):
                    if windows[c2] == needs[c2]:
                        match -= 1
                    windows[c2] -= 1
                left += 1

        return False
s1 = "adc"
s2 = "dcda"
c = Solution()
c.checkInclusion(s1,s2)