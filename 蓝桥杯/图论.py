from math import inf
# 建图模版-带权无向图
'''
[0,2,inf,3,inf]
[2,0,5,4,inf]
[inf,5,0,10,inf]
[3,4,10,0,7]
[inf,inf,inf,7,0]
'''
n, m = map(int, input().split())
g = [[inf] * n for _ in range(n)]
for _ in range(m):
    u, v, w = map(int, input().split())
    g[u][v] = g[v][u] = w
    g[u][u] = g[v][v] = 0

# 邻接表
'''
[(1, 2), (3, 3)]
[(0, 2), (2, 5), (3, 4)]
[(1, 5), (3, 10)]
[(0, 3), (1, 4), (4, 7), (2, 10)]
[(3, 7)]
'''
g = [[] for _ in range(n)]
for _ in range(m):
    u, v, w = map(int, input().split())
    g[u].append((v, w))
    g[v].append((u, w))

# 图的遍历
# DFS
s = set() # 访问过的点
def dfs(u):
    s.add(u)
    # 遍历u的所有邻居
    for v,_ in g[u]:
        if v not in s:
            dfs(v)

# 并查集
'''
class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]
        # def union(x, y):
        #     p[find(x)] = find(y)
        p = list(range(n))
        for u,v in edges:
            p[find(u)] = find(v)
        return find(source) == find(destination)''' 