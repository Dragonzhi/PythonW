import sys
input = lambda:sys.stdin.readline().strip()

'''
贪心
题目：https://www.luogu.com.cn/problem/P10387
'''
'''
#n数量，S团购价
n,S = map(int, input().split())
nums = [[0,0]] * n
#p价格，c次数
p, c = [0]*n, [0]*n

for i in range(n):
    nums[i] = list(map(int, input().split()))

nums.sort(key = lambda x:x[1])
for i in range(n):
    p[i], c[i] = nums[i][0], nums[i][1]
#res最少金币花销
res = cnt = 0
tot = sum(p)

for i in range(n):
    if tot >= S: #团购更便宜
        res += (c[i] - cnt) * S
        cnt = c[i]
    else: #每个人单独训练更便宜
        res += (c[i] - cnt) * p[i]
    tot -= p[i] #完成训练的，离开总花销
print(res)
'''

'''
排序
https://leetcode.cn/problems/queue-reconstruction-by-height/description/

# 指定升序降序
lit = [[1,3],[2,1],[3,2],[4,5],[5,6],[1,1],[2,3]]
lit.sort(key = lambda x : (-x[0], x[1]))
print(lit)
'''

people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2],[5,3]]
people.sort(key = lambda x:(-x[0], x[1]))
res = []
for i, p in enumerate(people):
    h, k = p[0], p[1]
    if k == i:
        res.append(p)
    elif k < i:
        res.insert(k, p)
print(res)
