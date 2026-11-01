import heapq

GOAL = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

def heuristic(state):
    distance = 0

    for i in range(9):
        tile = state[i]

        if tile != 0:
            goal = GOAL.index(tile)

            row1 = i // 3
            col1 = i % 3

            row2 = goal // 3
            col2 = goal % 3

            distance += abs(row1 - row2) + abs(col1 - col2)

    return distance

def get_neighbors(state):
    neighbors = []

    zero = state.index(0)
    row = zero // 3
    col = zero % 3

    moves = [
        (row - 1, col),
        (row + 1, col),
        (row, col - 1),
        (row, col + 1)
    ]

    for r, c in moves:
        if 0 <= r < 3 and 0 <= c < 3:
            new_pos = r * 3 + c

            new_state = list(state)
            new_state[zero], new_state[new_pos] = (
                new_state[new_pos], new_state[zero]
            )

            neighbors.append(tuple(new_state))

    return neighbors

def astar(start):
    pq = [(heuristic(start), 0, start, [start])]
    best_cost = {start: 0}

    while pq:
        f, g, state, path = heapq.heappop(pq)

        if state == GOAL:
            return path

        if g > best_cost[state]:
            continue

        for neighbor in get_neighbors(state):
            new_g = g + 1

            if new_g < best_cost.get(neighbor, float('inf')):
                best_cost[neighbor] = new_g
                new_f = new_g + heuristic(neighbor)

                heapq.heappush(
                    pq,
                    (new_f, new_g, neighbor, path + [neighbor])
                )

    return None

start = (1, 2, 3,
         4, 5, 6,
         7, 0, 8)

path = astar(start)

if path:
    print("Solution found!")
    print("Number of moves:", len(path) - 1)

    for state in path:
        for i in range(0, 9, 3):
            print(state[i:i + 3])
        print()
else:
    print("No solution found.")