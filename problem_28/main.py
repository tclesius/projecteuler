def spiral(k):
    grid = [[0 for _ in range(k)] for _ in range(k)]
    layer = center = k // 2
    num = 9
    cur_n = 5

    inner_grid = [[7, 8, 9], [6, 1, 2], [5, 4, 3]]
    for ir, r in enumerate(inner_grid):
        for ie, el in enumerate(r):
            grid[center - 1 + ir][center - 1 + ie] = el

    for x in range(1, layer):

        for i in range(cur_n - 1):
            num += 1
            grid[center - x + i][center + x + 1] = num

        for i in range(cur_n - 2):
            num += 1
            grid[center + x + 1][center + x - i] = num

        for i in range(-1, cur_n - 1):
            num += 1
            grid[center + x - i][center - x - 1] = num

        for i in range(cur_n - 1):
            num += 1
            grid[center - x - 1][center - x + i] = num

        cur_n += 2
    return grid


n = 1001
solution_grid = spiral(n)
print(sum([solution_grid[i][i] for i in range(n)]) + sum([solution_grid[i][-i - 1] for i in range(n)]) - 1)
