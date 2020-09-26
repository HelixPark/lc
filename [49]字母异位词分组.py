from typing import List
# utf-8
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 法1：排序数组分类的形式
        # 写法1：import collections
        # ans = collections.defaultdict(list)
        # # ans = {}
        # for s in strs:
        #     ans[tuple(sorted(s))].append(s)
        #
        # return ans.values()

        # 写法2
        # dic = {}
        # for s in strs:
        #     dic[tuple(sorted(s))] = dic.get(tuple(sorted(s)), []) + [s]
        #
        # return list(dic.values())

        # 写法3
        dic = {}
        for s in strs:
            keys = ''.join(sorted(s))
            if keys not in dic:
                dic[keys] = [s]
            else:
                dic[keys].append(s)
        return list(dic.values())


        # 法2：按计数也行，把s内的每个char转为ASCII码，存成tuple，其他和法1一样


strs =  ["eat", "tea", "tan", "ate", "nat", "bat"]
c = Solution()
c.groupAnagrams(strs)