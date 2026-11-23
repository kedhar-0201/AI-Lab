
from itertools import combinations
def cost(state):
    conflicts = 0
    n = len(state)
    for i in range(n):
        for j in range(i + 1, n):
            if (state[i] == state[j] or
                abs(state[i] - state[j]) == abs(i - j)):
                conflicts += 1
    return conflicts
def get_neighbours(state):
    neighbours = []
    for i, j in combinations(range(len(state)), 2):
        new_state = state[:]
        new_state[i], new_state[j] = new_state[j], new_state[i]
        neighbours.append((i, j, new_state, cost(new_state)))
    return neighbours
def hill_climbing():
    current = [3, 1, 2, 0]
    step = 1
    while True:
        current_cost = cost(current)
        print("\nStep:", step)
        print("Current State:", current)
        print("Current Cost:", current_cost)
        if current_cost == 0:
            print("\nGoal state reached!")
            print("Final State:", current)
            break
        neighbours = get_neighbours(current)
        print("\nNeighbour States and Costs:")
        for i, j, state, c in neighbours:
            print("Swap (x" + str(i) + ", x" + str(j) +
                  "):", state, "Cost:", c)
        best = min(neighbours, key=lambda x: (x[3], x[0], x[1]))
        if best[3] >= current_cost:
            print("\nLocal minimum reached. No better neighbour.")
            break
        print("\nSelected Swap: (x" +
              str(best[0]) + ", x" + str(best[1]) + ")")
        current = best[2]
        step += 1
hill_climbing()
