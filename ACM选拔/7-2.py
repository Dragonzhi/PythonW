'''
7-2 修车的最少时间
分数 10
作者 NWAFU-ACM队
单位 西北农林科技大学
给你一个整数数组 ranks ，表示一些机械工的 能力值 。ranks[i] 是第 i 位机械工的能力值。能力值为 r 的机械工可以在 r * (n^2) 分钟内修好 n 辆车。

同时给你一个整数 cars ，表示总共需要修理的汽车数目。

请你返回修理所有汽车 最少 需要多少时间。

注意：所有机械工可以同时修理汽车。

输入格式:
第一行给出两个整数n和m，n表示机械工的人数，m表示 需要修理的汽车的数量
第二行给出n个正整数表示工人的能力值。
n<=10^5
m<=10^6
能力值不超过100

输出格式:
输出修理所有汽车的最少时间（分钟）

输入样例 1:
4 10
4 2 3 1
输出样例 1:
16
样例解释:
第一位机械工修 2 辆车，需要 4 * 2 * 2 = 16 分钟。
第二位机械工修 2 辆车，需要 2 * 2 * 2 = 8 分钟。
第三位机械工修 2 辆车，需要 3 * 2 * 2 = 12 分钟。
第四位机械工修 4 辆车，需要 1 * 4 * 4 = 16 分钟。
16 分钟是修理完所有车需要的最少时间。
'''

import time
import psutil
import os

start_time = time.perf_counter()
# 获取程序开始时的内存使用量
process = psutil.Process(os.getpid())
start_memory = process.memory_info().rss

# 开始答题
n, cars = map(int, input().split())
ranks = list(map(int, input().split()))

start_time = time.perf_counter()
# 获取程序开始时的内存使用量
process = psutil.Process(os.getpid())
start_memory = process.memory_info().rss

left, right = 0, max(ranks) * cars * cars

while left < right:
    mid = (left + right) // 2
    total_cars = 0
    # 计算在 mid 时间内所有机械工能修理的汽车总数
    for r in ranks:
        total_cars += int((mid / r) ** 0.5)
    if total_cars >= cars:
        right = mid
    else:
        left = mid + 1

print(left)

# 计算时间
end_time = time.perf_counter()
# 获取程序结束时的内存使用量
end_memory = process.memory_info().rss
# 计算内存消耗（单位：字节）
memory_usage = end_memory - start_memory

print(f"\n程序运行时间为：{end_time - start_time} 秒")
print(f"程序内存消耗为：{memory_usage//8//1024} KB")