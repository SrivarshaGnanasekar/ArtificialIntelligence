import heapq

def heuristic(state, goal):
    return sum(abs(s % 3 - g % 3) + abs(s // 3 - g // 3) for s, g in zip(state, goal))

def get_neighbors(state):
    neighbors = []
    zero_index = state.index(0)
    row, col = zero_index // 3, zero_index % 3
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for move in moves:
        new_row, new_col = row + move[0], col + move[1]
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_index = new_row * 3 + new_col
            new_state = list(state)
            new_state[zero_index], new_state[new_index] = new_state[new_index], new_state[zero_index]
            neighbors.append(tuple(new_state))
    return neighbors

def a_star(start, goal):
    open_set = []
    heapq.heappush(open_set, (0 + heuristic(start, goal), 0, start, []))
    closed_set = set()
    while open_set:
        _, cost, current, path = heapq.heappop(open_set)
        if current in closed_set:
            continue
        path = path + [current]
        if current == goal:
            return path
        closed_set.add(current)
        for neighbor in get_neighbors(current):
            if neighbor not in closed_set:
                heapq.heappush(open_set, (cost + 1 + heuristic(neighbor, goal), cost + 1, neighbor, path))
    return None

def print_path(path):
    for state in path:
        for i in range(3):
            print(state[i*3:(i+1)*3])
        print()

start_state = (2,8,3,1,6,4,7,0,5)
goal_state = (1,2,3,8,0,4,7,6,5)

print("Initial State:")
print_path([start_state])

path = a_star(start_state, goal_state)

if path:
    print("Moves to reach the goal:")
    print_path(path)
    print("Goal Reached!")
else:
    print("No solution found.")
