import random
import math
def cost(board):
    conflicts = 0
    n = len(board)
    for i in range(n):
        for j in range(i + 1, n):
            if abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1
    return conflicts
def get_neighbor(board):
    new_board = board[:]
    i, j = random.sample(range(len(board)), 2)
    new_board[i], new_board[j] = new_board[j], new_board[i]
    return new_board
def simulated_annealing(n):
    current = list(range(n))
    random.shuffle(current)
    current_cost = cost(current)
    temperature = 100
    cooling_rate = 0.99
    min_temperature = 0.01
    best = current[:]
    best_cost = current_cost
    while temperature > min_temperature:
        if current_cost == 0:
            return current
        neighbor = get_neighbor(current)
        neighbor_cost = cost(neighbor)
        delta = neighbor_cost - current_cost
        if delta < 0:
            current = neighbor
            current_cost = neighbor_cost
        elif random.random() < math.exp(-delta / temperature):
            current = neighbor
            current_cost = neighbor_cost
        if current_cost < best_cost:
            best = current[:]
            best_cost = current_cost
        temperature *= cooling_rate
    if best_cost == 0:
        return best
    return None
def print_board(board, n):
    for row in range(n):
        for col in range(n):
            if board[col] == row:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
n = int(input("Enter number of queens: "))
if n == 2 or n == 3:
    print("No solution exists for", n, "queens.")
else:
    solution = simulated_annealing(n)
    if solution is not None:
        print("\nSolution found!")
        print("Final State:", solution)
        print("Final Cost:", cost(solution))
        print("\nChessboard:")
        print_board(solution, n)
    else:
        print("\nSolution not found. Try running again.")
