def canPartition2(self, nums: List[int]) -> bool:
    sum_nums = sum(nums)
    # 和为奇数，不可能划分为俩相等的
    if sum_nums % 2 != 0:
        return False

    # 划归为典型01背包，W相当于总容量，N物品数量，nums相当于物品重量，
    W = sum_nums // 2
    N = len(nums)

    dp = [[False] * (W + 1) for _ in range(N + 1)]

    for i in range(N + 1):
        dp[i][0] = True

    for i in range(1, N + 1):
        for w in range(1, W + 1):
            # 额度不够，放不下，不装
            if w < nums[i - 1]:
                dp[i][w] = dp[i - 1][w]
            else:
                # 不装入或装入
                dp[i][w] = dp[i - 1][w] | dp[i - 1][w - nums[i - 1]]

    return dp[N][W]