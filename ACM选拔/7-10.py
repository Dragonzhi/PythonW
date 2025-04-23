'''
7-10 求和游戏
分数 10
作者 NWAFU-ACM队
单位 西北农林科技大学
题目描述
爱丽丝和鲍勃正在玩一个游戏，他们有一个数组 a 
1
​
 ,a 
2
​
 ,…,a 
n
​
  . 游戏包括两个步骤：

首先，爱丽丝将从数组中移除最多k 个元素。
其次，鲍勃将把数组中的最多x个元素乘以 −1 .
爱丽丝希望最大化数组元素的和，而鲍勃希望最小化它。找到游戏结束后数组元素的总和，假设两位玩家均采用最优策略。

输入格式
每个测试包括多个测试用例。第一行包含一个整数t ( 1≤t≤10 
4
  ) — 测试用例的数量。接下来是测试用例的描述。

每个测试用例的第一行包含三个整数 n ,
k , 和x ( 1≤n≤2⋅10 
5
  , 1≤x,k≤n ) — 数组中的元素数量，爱丽丝可以移除的元素数量限制，以及鲍勃可以乘以−1 的元素数量限制。

每个测试用例的第二行包含n 个整数a 
1
​
 ,a 
2
​
 ,…,a 
n
​
  ( 1≤a 
i
​
 ≤1000 ) —
数组的元素。

保证所有测试用例中 n 的总和不超过2⋅10 
5
  .

输出格式
对于每个测试用例，输出一个整数 — 假设两位玩家都采取最优策略后，游戏结束后数组元素的总和。

输入输出样例 #1
输入 #1
8
1 1 1 
1 
4 1 1 
3 1 2 4 
6 6 3 
1 4 3 2 5 6 
6 6 1 
3 7 3 3 32 15 
8 5 3 
5 5 3 3 3 2 9 9 
10 6 4 
1 8 2 9 3 3 4 5 3 200
2 2 1 
4 3 
2 1 2 
1 3
输出 #1
0 
2 
0 
3 
-5 
-9 
0 
-1
说明/提示
在第一个测试案例中，爱丽丝移除数组中唯一的元素是最佳选择。游戏结束后，数组元素的总和为0。

在第二个测试案例中，爱丽丝最好不要删除任何元素。鲍勃将用 4 乘以−1 。因此数组元素的最终总和是 3+1+2−4=2 .

在第五个测试案例中，爱丽丝最好删除9,9。然后，鲍勃将用5,5,3 乘以−1 。因此数组元素的最终总和为−5−5−3+3+3+2=−5 .
'''

import time
start_time = time.perf_counter()
# 开始答题

t = int(input())
for _ in range(t):
    n, k, x = map(int, input().split())
    arr = list(map(int, input().split()))
    # 爱丽丝移除元素
    best_sum = float('-inf')
    from itertools import combinations
    # 遍历移除 0 到 k 个元素的所有组合
    for remove_num in range(k + 1):
        for remove_comb in combinations(range(n), remove_num):
            new_arr = [arr[i] for i in range(n) if i not in remove_comb]
            new_arr.sort()
            # 鲍勃选择元素乘以 -1
            new_sum = sum(new_arr)
            for j in range(min(x, len(new_arr))):
                new_sum -= 2 * new_arr[j]
            best_sum = max(best_sum, new_sum)
    print(best_sum)


# 计算时间
end_time = time.perf_counter()
print(f"\n程序运行时间为：{end_time - start_time} 秒")


'''


超时一个
t = int(input())
def find(n, k, x, ns):
    ns.sort()
    r = []
    for i in range(k+1):
        tns = [x for x in ns]
        for _ in range(i):
            tns.pop()
            if len(tns) == 0:
                break
        if len(tns) == 0:
            tns.append(0)
        else:
            if x <= len(tns):
                for dx in range(1,x+1):
                    tns[-dx] *= -1
            else:
                for dx in range(1,len(tns)+1):
                    tns[-dx] *= -1
        r.append(sum(tns))
    return max(r)
for z in range(t-1):
    n, k, x = map(int, input().split())
    ns = list(map(int, input().split()))
    print(find(n, k, x, ns),end=' \n')
n, k, x = map(int, input().split())
ns = list(map(int, input().split()))
print(find(n, k, x, ns),end='')


'''