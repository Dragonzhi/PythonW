'''
7-7 相同奇偶性
分数 10
作者 NWAFU-ACM队
单位 西北农林科技大学
题目描述
定义一个序列的 权值 等于这个序列所有的元素之和。

试判断：是否存在一个长度为 n 的 排列，满足以下约束条件？

其所有长度为 k 的 子区间 的权值具有相同的奇偶性。
输入格式
第一行一个整数 T (1⩽T⩽10 
5
 )，表示测试数据组数。
对于每个测试用例，唯一的行包含两个整数 n
,k (1⩽n,k⩽10 
9
 )

输出格式
对于每组测试数据，输出一行一个字符串。若存在符合题意的排列，输出 yes；否则，输出
no。

样例解释
对于第一组测试数据，能够证明不存在任何符合题意的排列。

对于第二组测试数据，[1,2,3,4] 是一个符合题意的排列。其所有长度为 2 的子区间分别为
[1,2],[2,3],[3,4]，它们的权值分别为
3,5,7，具有相同的奇偶性。

对于第三组测试数据，[1,2,3,5,4] 是一个符合题意的排列。其所有长度为 3 的子区间分别为
[1,2,3],[2,3,5],[3,5,4]，它们的权值分别为
6,10,12，具有相同的奇偶性。

输入输出样例 #1
输入 #1
3
3 1
4 2
5 3
输出 #1
no
yes
yes
'''

import time
start_time = time.perf_counter()
# 开始答题
def can_have_same_parity(n, k):
    if k % 2 == 0:
        return True
    elif n % 2 == 0:
        return True
    else:
        return False

T = int(input())
results = []
for _ in range(T):
    n, k = map(int, input().split())
    if can_have_same_parity(n, k):
        results.append("yes")
    else:
        results.append("no")

for result in results:
    print(result)

# 计算时间
end_time = time.perf_counter()
print(f"\n程序运行时间为：{end_time - start_time} 秒")
