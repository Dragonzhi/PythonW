import sys
input = lambda:sys.stdin.readline().strip()

'''
爬楼梯
（递归，动态规划，记忆化搜索）
'''

import time
import psutil
import os

start_time = time.perf_counter()
# 获取程序开始时的内存使用量
process = psutil.Process(os.getpid())
start_memory = process.memory_info().rss


# 开始答题

# 递归暴力解决，时间复杂度为O(2^n)，容易超时

def dfs(n):
    if n == 1 or n == 0:
        return 1
    return dfs(n-1) + dfs(n-2)
print(dfs(36))


end_time = time.perf_counter()
# 获取程序结束时的内存使用量
end_memory = process.memory_info().rss
# 计算内存消耗（单位：字节）
memory_usage = end_memory - start_memory

print(f"\n程序运行时间为：{end_time - start_time} 秒")
print(f"程序内存消耗为：{memory_usage} 字节")
# # 记忆化搜索，时间复杂度为O(n)

# start_time = time.perf_counter()
# from functools import *
# # @lru_cache(maxsize=None) # 使用lru_cache缓存函数结果，避免重复计算
# @cache
# def dfs(n):
#     if n == 1 or n == 0:
#         return 1
#     return dfs(n-1) + dfs(n-2)
# print(dfs(35))

# # 计算时间
# end_time = time.perf_counter()
# print(f"\n程序运行时间为：{end_time - start_time}秒")
# nums = [2,7,9,3,1]
# l = len(nums)   
# if l % 2:
#     lst = [x for i, x in enumerate(nums) if i % 2 == 0]
#     print(lst)
# else:
#     lst = [x for i, x in enumerate(nums) if i % 2 == 0]
#     print(lst)
# print(sum(lst))

# end_time = time.perf_counter()
# print(f"\n程序运行时间为：{end_time - start_time}秒")
'''
打家劫舍
https://leetcode.cn/problems/house-robber/
'''

# nums = [1, 99, 1, 1, 99, 1, 99]
# n = len(nums)
# f = [[0] * 2 for _ in range(n + 1)]
# print(f)
# for i in range(1, n + 1):
#     f[i][0] = max(f[i-1][0], f[i-1][1])
#     print("f[i][0]",f)
#     f[i][1] = f[i-1][0] + nums[i-1]
#     print("f[i][1]",f)
# print(max(f[n][0], f[n][1]))

# end_time = time.perf_counter()
# print(f"\n程序运行时间为：{end_time - start_time}秒")


