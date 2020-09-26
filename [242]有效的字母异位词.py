
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
         return True if  ''.join(sorted(s)) == ''.join(sorted(t)) else False