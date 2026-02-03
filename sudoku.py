import numpy as np

def print_grid(grid):
    for r in grid:
        print(" ".join(str(num) if num != 0 else '.' for num in r))

def is_safe(grid, r, c, n):
    if n in grid[r]:
        return False
    if n in grid[:, c]:
        return False
    b_r_s = (r // 3) * 3
    c_r_s = (c // 3) * 3
    if n in grid[b_r_s:b_r_s + 3, c_r_s:c_r_s + 3]:
        return False
    return True

def find(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return (i, j)
    return None

def solve(grid):
    emp = find(grid)
    if not emp:
        return True
    r, c = emp
    for n in range(1, 10):
        if is_safe(grid, r, c, n):
            grid[r][c] = n

            if solve(grid):
                return True

            grid[r][c] = 0
    return False

def get_input():
    print("Enter sudoku puzzle (Enter 0 for empty cells):")
    grid = []
    for i in range(9):
        while True:
            try:
                r = list(map(int, input(f"Row{i + 1}:").strip().split()))
                if (len(r) != 9 or any(n < 0 or n > 9 for n in r)):
                    raise ValueError
                grid.append(r)
                break
            except ValueError:
                print("Invalid numbers")
    return np.array(grid)

s = get_input()
print("Sudoku puzzle:")
print_grid(s)
if solve(s):
    print("Solved puzzle:")
    print_grid(s)
else:
    print("No solution found")
