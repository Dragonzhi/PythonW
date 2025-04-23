'''
7-9 Horizon Blue
分数 10
作者 NWAFU-ACM队
单位 西北农林科技大学
题目描述
小 C 喜欢在画板上画画。他进行了 n 次操作，每次操作有如下三种可能：

1 k b 代表小 C 绘制了一条解析式为 y=kx+b 的直线。
2 k b 代表小 C 询问你直线 y=kx+b 与多少条被绘制的直线有恰好一个公共点。
3 k b 代表小 C 擦除所有与直线 y=kx+b 有至少一个公共点的直线。
注意：两条重合的直线有无数个交点。

注意：询问时重合的直线应分别计算。

输入格式
第一行一个整数 n。

接下来 n 行，每行三个整数 1/2/3,k,b，代表一次操作。
1≤n≤10 
5
 ，1≤∣k∣≤10 
5
 ，0≤∣b∣≤10 
5
 。

输出格式
对每次 2 k b 操作，输出满足要求的直线数量。

输入输出样例 #1
输入 #1
6
1 1 0 
1 -1 0 
2 2 1 
3 1 3 
2 2 1 
2 1 1
输出 #1
2 
1 
0
输入输出样例 #2
输入 #2
10 
1 1 0 
1 1 0 
2 1 1
2 1 0 
2 2 5 
3 1 0 
2 2 5 
1 2 3 
1 3 4 
2 3 5
输出 #2
0 
0 
2 
0 
1
说明/提示
【样例 1 解释】
第 1 次操作，绘制直线 y=x。
第 2 次操作，绘制直线 y=−x。
第 3 次操作，可以发现直线 y=2x+1 与前两条线相交。
第 4 次操作，擦掉所有 y=x+3 相交的线，直线 y=−x
被擦掉。
第 5 次操作，y=2x+1 显然与 y=x 相交。
第 6 次操作，y=x+1 与 y=x 斜率相等，是平行线，不相交。
'''

import time
start_time = time.perf_counter()
# 开始答题

n = int(input())
# 存储已经绘制的直线，每个元素是一个元组 (k, b)
lines = []

for _ in range(n):
    op, k, b = map(int, input().split())
    if op == 1:
        # 绘制直线
        lines.append((k, b))
    elif op == 2:
        # 询问直线与多少条已绘制直线有恰好一个公共点
        count = 0
        for line in lines:
            line_k, line_b = line
            if k != line_k:
                # 斜率不同，有一个公共点
                count += 1
        print(count)
    elif op == 3:
        # 擦除所有与直线 y=kx+b 有至少一个公共点的直线
        new_lines = []
        for line in lines:
            line_k, line_b = line
            if k == line_k and b != line_b:
                # 斜率相同但截距不同，平行，保留
                new_lines.append(line)
        lines = new_lines


# 计算时间
end_time = time.perf_counter()
print(f"\n程序运行时间为：{end_time - start_time} 秒")
