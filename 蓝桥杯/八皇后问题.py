def total_n_queens(n):
    def backtrack(row, cols, diag1, diag2):
        nonlocal count
        if row == n:
            count += 1
            return
        for col in range(n):
            # 检查当前列和两条对角线是否已被占用
            if col not in cols and (row - col) not in diag1 and (row + col) not in diag2:
                # 递归到下一行，并记录占用信息
                backtrack(row + 1, cols | {col}, diag1 | {row - col}, diag2 | {row + col})
    
    count = 0  # 初始化计数器
    backtrack(0, set(), set(), set())  # 从第0行开始搜索
    return count

print(total_n_queens(8))