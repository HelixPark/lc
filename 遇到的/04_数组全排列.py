# utf-8
from typing import List
def permute(nums: List[int]) -> List[List[int]]:
    # 全排列：first可代表深度，这里描述为数组长度
    def backtrack(first=0, curr=[]):
        # 符合条件，排列完成
        if len(curr) == l:
            return res.append(curr[:])

        # 遍历选择列表
        for i in range(0, l):
            # 检查是否被访问过
            if visited[i] == True:
                continue
            # 选择:
            curr.append(nums[i])
            visited[i] = True
            # 回溯
            backtrack(first + 1, curr)
            # 撤销选择
            curr.pop()
            visited[i] = False

    res, l = [], len(nums)
    visited = [False] * l
    backtrack()
    # return res
    count = 0
    for i in range(len(res)):
        tmp = 0
        for j in range(l):
            tmp = res[i][j] * 10**(l-j-1) + tmp
        if tmp % 7 == 0:
            count += 1
    return count

nums = [1,1,2]
res = permute(nums)
print(res)