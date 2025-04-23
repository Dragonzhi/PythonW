'''7-6 八宝粥行动
分数 10
作者 NWAFU-ACM队
单位 西北农林科技大学
Vulpes的电脑上有一款搜打撤游戏。
Vulpes致力于将他看到的一切物品放入他的背包。但Vulpes的大脑容易过载，在向背包里放入新物品时并不会移动原有物品。给你Vulpes的背包现状，以及Vulpes遇到的新物品大小，请你判断Vulpes是否会将新物品放入背包。

输入格式:
第一行给出正整数t(1≤t≤100)，表示有t组数据。
对于每组数据：
第一行给出vulpes的背包大小m,n(1≤m≤1000,1≤n≤1000)；要放入的物品的大小a,b(1≤a≤1000,1≤b≤1000)；
接下来m行，每行n个字符，来描述背包的当前状况。0代表当前位置为空，1代表当前位置已放入物品。
保证所有数据中m∗n的和不超过1000000。

输出格式:
每组样例单独输出一行。若Vulpes将物品放入背包，输出1，否则输出0。

输入样例:
2
3 5 2 3
10011
10010
10010
3 4 2 3
1111
0100
0010
输出样例:
1
0
 

样例解释:
该样例中有两组测试样例。第一组背包空间大小为3∗5，要放入的物品大小为2∗3，可以找到连续足够的空间放入该物品；第二组背包空间大小为3∗4，要放入的物品大小为2∗3，不可以找到连续足够的空间放入该物品。
'''

import time
start_time = time.perf_counter()
# 开始答题
def can_place_item_prefix_sum(m, n, a, b, backpack):
    # 构建前缀和数组
    prefix = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            prefix[i][j] = prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1] + (1 if backpack[i - 1][j - 1] == '1' else 0)
    
    # 检查每个可能的区域
    for i in range(m - a + 1):
        for j in range(n - b + 1):
            # 计算区域中已放入物品的数量
            total = prefix[i + a][j + b] - prefix[i][j + b] - prefix[i + a][j] + prefix[i][j]
            if total == 0:
                return 1
    return 0
# 读取输入
t = int(input())
for _ in range(t):
    # 读取背包大小和物品大小
    m, n, a, b = map(int, input().split())
    # 读取背包状态
    backpack = []
    for _ in range(m):
        row = input().strip()
        backpack.append(list(row))
    # 判断是否可以放入
    result = can_place_item_prefix_sum(m, n, a, b, backpack)
    # 输出结果
    print(result)
# 计算时间
end_time = time.perf_counter()
print(f"\n程序运行时间为：{end_time - start_time} 秒")
