'''
统计相似字符串对的数目
https://leetcode.cn/problems/count-pairs-of-similar-strings/solutions/3065403/tong-ji-xiang-si-zi-fu-chuan-dui-de-shu-djtsd/?envType=daily-question&envId=2025-03-29

collections模块 Counter 对象
'''
# from collections import Counter

# words = ["dcedceadceceaeddcedc", "dddcebcedcdbaeaaaeab", "eecbeddbddeadcbbbdbb",
#          "decbcbebbddceacdeadd", "ccbddbaedcadedbcaaae", "dddcaadaceaedcdceedd",
#          "bbeddbcbbccddcaceeea", "bdabacbbdadabbbddaea"]
# # 创建一个 Counter 对象
# cnt = Counter()
# for i in words:
#     # 生成排序后的元组
#     w = tuple(sorted(set(i)))
#     # 使用 Counter 对象统计元组出现次数
#     cnt[w] += 1

# print(cnt)
# res = 0
# for c in cnt:
#     if cnt[c] >= 2:
#         res += (cnt[c] * (cnt[c] - 1)) // 2
# print(res)

'''
Python中 collections模块的详细用法介绍
https://blog.csdn.net/qdpython/article/details/120786550


python标准库之itertools模块
https://blog.csdn.net/xcntime/article/details/115675908
'''

# from itertools import *
# x = accumulate(range(10))
# print(list(x))
# [0, 1, 3, 6, 10, 15, 21, 28, 36, 45]
'''
1、itertools.product(*iterable[,repeat])
这个工具就是产生多个列表或者迭代器的n维积。如果没有特别指定repeat默认为列表和迭代器的数量。

 

    例：
    import itertools
    a = (1, 2, 3)
    b = ('A', 'B', 'C')
    c = itertools.product(a,b)
    for elem in c:
        print elem
    输出为：
    (1, 'A')
    (1, 'B')
    (1, 'C')
    (2, 'A')
    (2, 'B')
    (2, 'C')
    (3, 'A')
    (3, 'B')
    (3, 'C')

2、itertools.permutations(iterable[,r])
这个函数作用其实就是产生指定数目repeat的元素的所有排列，且顺序有关，但是遇到原列表或者迭代器有重复元素的现象的时候，也会对应的产生重复项。这个时候最好用groupby或者其他filter去一下重，如果有需要的话。

 

    例：
    import itertools
    x = itertools.permutations(range(4), 3)
    print(list(x))
    输出为：
    [(0, 1, 2), 
    (0, 1, 3), 
    (0, 2, 1), 
    (0, 2, 3), 
    (0, 3, 1), 
    (0, 3, 2), 
    (1, 0, 2), 
    (1, 0, 3), 
    (1, 2, 0), 
    (1, 2, 3), 
    (1, 3, 0), 
    (1, 3, 2), 
    (2, 0, 1), 
    (2, 0, 3), 
    (2, 1, 0), 
    (2, 1, 3), 
    (2, 3, 0), 
    (2, 3, 1), 
    (3, 0, 1),
    (3, 0, 2), 
    (3, 1, 0), 
    (3, 1, 2), 
    (3, 2, 0), 
    (3, 2, 1)
    ]
3、itertools.combinations(iterable,r)
这个函数用来生成指定数目r的元素不重复的所有组合。注意和permutation的区分，以及这个组合是无序的，只考虑元素本身的unique性。

 

    例：
    import itertools
    x = itertools.combinations(range(4), 3)
    print(list(x))
    输出为：
    [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)]
4、itertools.combinations_with_replacement(iterable,r)
这个函数用来生成指定数目r的元素可重复的所有组合。然而这个函数依然要保证元素组合的unique性。

 

    例：
    import itertools
    x = itertools.combinations_with_replacement('ABC', 2)
    print(list(x))
    输出为：
    [('A', 'A'), 
    ('A', 'B'), 
    ('A', 'C'), 
    ('B', 'B'), 
    ('B', 'C'), 
    ('C', 'C’)
    ]

————————————————

                            版权声明：本文为博主原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接和本声明。
                        
原文链接：https://blog.csdn.net/xcntime/article/details/115675908
'''
# -------------------------------------------------------------

'''
 bisect 模块
bisect 模块提供了二分查找算法，用于在有序序列中查找元素的插入位置。二分查找的时间复杂度为 $O(log n)$，在处理大规模有序数据时非常高效。

import bisect

# 有序列表
nums = [1, 3, 5, 7, 9]

# 查找元素插入位置(第一个比4大的元素位置)
pos = bisect.bisect_left(nums, 4)
print(pos)
# 输出：2
'''

'''
heapq 模块
heapq 模块实现了堆队列算法，也称为优先队列算法。堆是一种特殊的树形数据结构，每个节点都比其子节点小（小顶堆）。在算法竞赛中，它常用于解决需要快速找到最小或最大元素的问题。

示例代码：

'''
# import heapq

# # 创建一个堆
# heap = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# heapq.heapify(heap)

# # 弹出最小元素
# smallest = heapq.heappop(heap)
# print(smallest)

# # 插入新元素
# heapq.heappush(heap, 0)
# print(heap)


'''
functools 模块
functools 模块提供了一些高阶函数，例如 reduce()、lru_cache() 等。lru_cache() 可以实现函数结果的缓存，避免重复计算，在递归算法中能显著提高性能。
'''
# import functools

# @functools.lru_cache(maxsize=None)
# def fibonacci(n):
#     if n <= 1:
#         return n
#     return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(10))

'''
from fractions import Fraction

# 创建分数对象
a = Fraction(1, 2)
b = Fraction(1, 3)

# 分数加法
result = a + b
print(result)
'''

from fractions import Fraction

# 创建分数对象
a = Fraction(1, 2)
b = Fraction(1, 3)

# 分数加法
result = a + b
print(result)
