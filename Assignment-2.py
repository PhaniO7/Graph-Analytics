def maxRegion(grid):
    n = len(grid)
    m = len(grid[0])
    visited = [[False]*m for _ in range(n)]

    def dfs(r, c):
        stack = [(r, c)]
        visited[r][c] = True
        count = 0
        while stack:
            cr, cc = stack.pop()
            count += 1
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    if dr == 0 and dc == 0:
                        continue
                    nr, nc = cr + dr, cc + dc
                    if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and grid[nr][nc] == 1:
                        visited[nr][nc] = True
                        stack.append((nr, nc))
        return count

    best = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1 and not visited[i][j]:
                best = max(best, dfs(i, j))
    return best


if __name__ == "__main__":
    n = int(input())
    m = int(input())
    grid = []
    for _ in range(n):
        grid.append(list(map(int, input().split())))
    print(maxRegion(grid))