s = '0110'

from itertools import pairwise

def minimumCost(s: str) -> int:
    # 计算所有相邻不相等字符对的最小反转成本之和
    return sum(min(i, len(s) - i) for i, (x, y) in enumerate(pairwise(s), 1) if x != y)

print(minimumCost(s))