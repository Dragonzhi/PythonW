from itertools import combinations

def generate_subsets_itertools(lst):
    subsets = []
    for r in range(len(lst) + 1):
        subsets.extend(combinations(lst, r))
    return [list(subset) for subset in subsets]

# 测试代码
lst = [1, 2, 3]
result = generate_subsets_itertools(lst)
print(result)
