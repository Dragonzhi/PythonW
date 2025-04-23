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

# 计算时间
end_time = time.perf_counter()
# 获取程序结束时的内存使用量
end_memory = process.memory_info().rss
# 计算内存消耗（单位：字节）
memory_usage = end_memory - start_memory

print(f"\n程序运行时间为：{end_time - start_time} 秒")
print(f"程序内存消耗为：{memory_usage//8} B")