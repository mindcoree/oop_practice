from collections import deque


def solve_bacteria(grid):
    if not grid or not grid[0]:
        return -1

    rows, cols = len(grid), len(grid[0])
    que = deque()
    visited = [[-1 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                que.append((i, j))
                visited[i][j] = 0

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    # BFS
    max_time = 0
    while que:
        x, y = que.popleft()
        current_time = visited[x][y]

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (0 <= nx < rows and 0 <= ny < cols and
                    grid[nx][ny] != '#' and visited[nx][ny] == -1):
                visited[nx][ny] = current_time + 1
                max_time = max(max_time, visited[nx][ny])
                que.append((nx, ny))

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0 and visited[i][j] == -1:
                return -1

    return max_time if max_time > 0 else 0


grid = [
    [0, 0, 1],
    [1, 1, 1],
    [0, 0, 0],
]

print(solve_bacteria(grid))