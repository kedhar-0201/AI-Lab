import heapq
goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)
def heuristic(state):
    distance = 0
    for i in range(9):
        if state[i] != 0:
            value = state[i]
            current_row = i // 3
            current_col = i % 3
            goal_row = (value - 1) // 3
            goal_col = (value - 1) % 3
            distance += abs(current_row - goal_row)
            distance += abs(current_col - goal_col)
    return distance
def get_neighbors(state):
    neighbors = []
    zero = state.index(0)
    row = zero // 3
    col = zero % 3
    moves = [
        (-1, 0),  
        (1, 0),   
        (0, -1),  
        (0, 1)    
    ]
    for dr, dc in moves:
        new_row = row + dr
        new_col = col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_pos = new_row * 3 + new_col
            new_state = list(state)
            new_state[zero], new_state[new_pos] = (
                new_state[new_pos], new_state[zero]
            )
            neighbors.append(tuple(new_state))
    return neighbors
def astar(start):
    pq = []
    heapq.heappush(pq, (heuristic(start), 0, start))
    visited = set()
    parent = {}
    g_cost = {start: 0}
    while pq:
        f, g, current = heapq.heappop(pq)
        if current in visited:
            continue
        visited.add(current)
        if current == goal:
            path = []
            while current in parent:
                path.append(current)
                current = parent[current]
            path.append(start)
            path.reverse()
            print("\nSolution Found!")
            print("Number of moves:", len(path) - 1)
            for step, state in enumerate(path):
                print("\nStep", step)
                print_board(state)
            return
        for neighbor in get_neighbors(current):
            new_g = g + 1
            if neighbor not in g_cost or new_g < g_cost[neighbor]:
                g_cost[neighbor] = new_g
                parent[neighbor] = current
                h = heuristic(neighbor)
                new_f = new_g + h
                heapq.heappush(
                    pq, (new_f, new_g, neighbor)
                )
    print("No solution found!")
def print_board(state):
    for i in range(0, 9, 3):
        print(state[i], state[i+1], state[i+2])
print("Enter the initial state (0 represents blank):")
start = tuple(map(int, input().split()))
if len(start) != 9 or sorted(start) != list(range(9)):
    print("Invalid puzzle state!")
else:
    astar(start)
