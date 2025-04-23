##from bisect import *
import sys
input = lambda: sys.stdin.readline().strip()
'''
二分
11 3
1 3 3 3 5 7 9 11 13 15 15
1 3 6

1 2 -1
'''
##
##n, m = map(int, input().split())
##nums = list(map(int, input().split()))
##Q = list(map(int, input().split()))
##
####nums = [1,9,9,9,10,15,100,500]
##s = set(nums)
##for q in Q:
##    if q not in s:
##        print(-1, end = " ")
##    else:
##        print(bisect(nums, q-1) + 1, end = " ")
'''
朴素二分
'''
## *****重点默写
'''
def bisect(a, x, lo=0, hi=None):
    if hi is None: hi = len(a)
    while lo < hi:
        i = (lo + hi) >> 1 #中位数 >> 1 等价于 //2
        if a[i] > x:
            hi = i
        else:
            lo = i + 1
    return lo
'''

##def bisect(a, x, lo=0, hi = None):
##    if hi == None: hi = len(a)
##    while lo < hi:
##        i = (lp + hi) >> 1
##        if a[i] > x:
##            hi = i
##        else:
##            lo = i + 1
##    return lo

'''
二分实践

0 1 7 4 4 5
3 6

6
'''
##
##nums = list(map(int, input().split()))
##lower, upper = map(int, input().split())
##re = 0
##nums.sort()
##for i, x in enumerate(nums):
##    L = bisect(nums, lower-x-1, i + 1)
##    R = bisect(nums, upper-x, i + 1)-1
##    re += R-L+1
####    print(a, x, L,R,re)
##print(re)

'''
朴素二分check

a = [1,9,9,9,15,100,500]
##b = [x**3 + x*2 + 1 for x in a]
def bisect(a, x, lo=0, hi=None, check = lambda y: y):
    if hi is None: hi = len(a)
    while lo < hi:
        i = (lo + hi) >> 1 #中位数 >> 1 等价于 //2
        if check(a[i]) > x:
            hi = i
        else:
            lo = i + 1
    return lo
print(bisect(a, 3408, check = lambda y: y**3 + y*2 + 1))
##print(bisect(b, 3408))
'''

'''
二分答案
'''
##def f(x):
##    return x**3 + x + 1
##def bisect(lo, hi, target, check):
##    while lo < hi:
##        i = (lo + hi) >> 1
##        if check(i, target):
##            hi = i
##        else:
##            lo = i + 1
##    return lo
##
##target = 114514
##res = bisect(1, 10**8, target, lambda x, target: f(x) > target)
##print(res)
##print(f(res))
##print(f(res-1))
'''
class solution:
    def maxCandies(a: list, k):
        if sum(a) < k : return 0
        lo, hi = 1, 10 ** 12 + 10
        def check(res):
            return sum(x // res for x in a) < k
        while lo < hi:
            i = (lo + hi) >> 1
            if check(i): hi = i
            else: lo = i + 1
        return lo - 1

print(solution.maxCandies([5,8,6], 3)) 
'''
