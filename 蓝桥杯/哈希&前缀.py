import sys
input = lambda:sys.stdin.readline().strip()

'''
哈希
https://leetcode.cn/problems/two-sum/description/?envType=problem-list-v2&envId=o85r8WFa
'''
##nums = [2,15,11,7]
##target = 9
##
##d = {}
##def target_sum(nums, target):
##    for i, x in enumerate(nums):
##        if d.get(target - x) is not None:
##            return [i, d[target - x]]
##        d[x] = i
####        print(d)
##print(target_sum(nums, target))

'''
前缀和
https://www.luogu.com.cn/problem/P8218
'''

##n = int(input())
##a = list(map(int, input().split()))
##m = int(input())
##
##p = [0] * (n + 1)
##for i in range(n):
##    p[i+1] = p[i] + a[i]
####    print(p)
##for _ in range(m):
##    l, r = map(int, input().split())
##    print(p[r] - p[l-1])
