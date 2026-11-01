from collections import deque

grid = [
    ['S', '.', '#', '.'],
    ['.', '.', '#', '.'],
    ['#', '.', '.', '.'],
    ['.', '#', '.', 'G']
]

start = (0, 0)
goal = (3, 3)

queue = deque([(start, [start])])
visited = {start}

while queue:
    position, path = queue.popleft()

    if position == goal:
        print("Path found:")
        print(path)
        print("Number of moves:", len(path) - 1)
        break

    row, col = position

    moves = [
        (row - 1, col),
        (row + 1, col),
        (row, col - 1),
        (row, col + 1)
    ]

    for r, c in moves:
        if (0 <= r < len(grid) and
            0 <= c < len(grid[0]) and
            grid[r][c] != '#' and
            (r, c) not in visited):

            visited.add((r, c))
            queue.append(((r, c), path + [(r, c)]))

else:
    print("No path found.")