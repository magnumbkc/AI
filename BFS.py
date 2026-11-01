from collections import deque

graph = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1, 6],
    4: [2],
    5: [2, 6],
    6: [3, 5]
}

start = 1
goal = 6

queue = deque([(start, [start])])
visited = {start}

while queue:
    node, path = queue.popleft()

    if node == goal:
        print("Path found:", path)
        print("Number of edges:", len(path) - 1)
        break

    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append((neighbor, path + [neighbor]))

else:
    print("Goal not reachable.")