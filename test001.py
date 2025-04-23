def count_arrangements(n, k):
    # 取模数
    mod = 10**9 + 7
    # 初始化二维数组
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    # 没有画时，恰好能看到0幅画的摆放方式数量为1
    dp[0][0] = 1
    
    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            # 状态转移方程
            dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j] * (i - 1)) % mod
    
    return dp[n][k]

# 测试样例
print(count_arrangements(4, 2))  # 输出: 11
print(count_arrangements(6, 3))  # 输出: 225
print(count_arrangements(7, 4))  # 输出: 735
print(count_arrangements(9, 5))  # 输出: 22449
