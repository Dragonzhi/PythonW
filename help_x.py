N = int(input())
p = float(input())
min_expected = float('inf')
best_K = 1
for K in range(1, N + 1):
    if N % K == 0:
        groups = N // K
        x = 1 - (1 - p) ** K
        expected = groups * (1 + x * (K - 1))
        if expected < min_expected:
            min_expected = expected
            best_K = K
print(best_K)