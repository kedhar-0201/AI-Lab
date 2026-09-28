from collections import deque
GOAL = (
    1, 2, 3,
    4, 5, 6,
    7, 8, 0
)
def get_neighbors(state):
    neighbors = []
    zero = state.index(0)
    row, col = divmod(zero, 3)
    moves = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)\
            ]
    for dr, dc in moves:
        new_row = row + dr
        new_col = col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_pos = new_row * 3 + new_col
            new_state = list(state)
            new_state[zero], new_state[new_pos] = \
                new_state[new_pos], new_state[zero]
            neighbors.append(tuple(new_state))                       
    return neighbors
def bfs(start):
    queue = deque()
    queue.append((start, [start]))
    visited = set()
    visited.add(start)
    while queue:
        state, path = queue.popleft()
        if state == GOAL:
            return path
        for next_state in get_neighbors(state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append(
                    (next_state, path + [next_state])
                )
    return None
def dfs(start):
    stack = []
    stack.append((start, [start]))
    visited = set()
    while stack:
        state, path = stack.pop()
        if state == GOAL:
            return path
        if state in visited:
            continue
        visited.add(state)
        for next_state in get_neighbors(state):
            if next_state not in visited:
                stack.append(
                    (next_state, path + [next_state])
                )
    return None
def print_puzzle(state):
    for i in range(0, 9, 3):
        print(state[i:i + 3])
    print()
start = (
    1, 2, 3,
    4, 0, 6,
    7, 5, 8
)
print("========================================")
print("           8 PUZZLE SOLVER")
print("========================================")
print("\nInitial State:")
print_puzzle(start)
print("========================================")
print("                 BFS")
print("========================================")
bfs_path = bfs(start)
if bfs_path is not None:
    print("Number of moves:", len(bfs_path) - 1)
    print("\nBFS Solution:\n")
    for step, state in enumerate(bfs_path):
        print("Step", step)
        print_puzzle(state)
else:
    print("No solution found using BFS.")
print("========================================")
print("                 DFS")
print("========================================")
dfs_path = dfs(start)
if dfs_path is not None:
    print("Number of moves:", len(dfs_path) - 1)
    print("\nDFS Initial State:")
    print_puzzle(dfs_path[0])
    print("DFS Final State:")
    print_puzzle(dfs_path[-1])
else:
    print("No solution found using DFS.")