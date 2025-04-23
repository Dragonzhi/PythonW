import time
import psutil
import os
import sys
input = lambda:sys.stdin.readline().strip()

start_time = time.perf_counter()
# 获取程序开始时的内存使用量
process = psutil.Process(os.getpid())
start_memory = process.memory_info().rss

# 开始答题

import math

# 读取输入
n, k, T = map(int, input().split())
scores = list(map(int, input().split()))

# 定义计算方差的函数
def variance(arr):
    mean = sum(arr) / len(arr)
    return sum((x - mean) ** 2 for x in arr) / len(arr)

# 遍历检查人数
for x in range(k, n + 1):
    from itertools import combinations
    # 生成所有可能的 k 人组合
    combos = combinations(scores[:x], k)
    for combo in combos:
        # 计算方差
        var = variance(combo)
        if var < T:
            # 找到满足条件的组合，输出结果
            print(x)
            break
    else:
        continue
    break
else:
    # 没有找到满足条件的组合，输出 -1
    print(-1)


# 计算时间
end_time = time.perf_counter()
# 获取程序结束时的内存使用量
end_memory = process.memory_info().rss
# 计算内存消耗（单位：字节）
memory_usage = end_memory - start_memory

print(f"\n程序运行时间为：{end_time - start_time} 秒")
print(f"程序内存消耗为：{memory_usage//8} B")