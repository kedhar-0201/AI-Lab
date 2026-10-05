def depth_limited_search(graph, node, goal, limit, path):       
    if node == goal:
        return path
    if limit == 0:
        return None
    for child in graph.get(node, []):
        if child not in path:
            result = depth_limited_search(
                graph,
                child,
                goal,
                limit - 1,
                path + [child]
            )
            if result is not None:
                return result
    return None
def iterative_deepening_search(graph, start, goal):
    depth = 0
    while True:
        result = depth_limited_search(
            graph,
            start,
            goal,
            depth,
            [start]
        )
        if result is not None:
            return result
        depth += 1
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': ['H', 'K'],
    'F': ['H', 'K', 'L'],
    'G': [],
    'H': [],
    'K': [],
    'L': []
}
start = 'A'
goal = 'G'
result = iterative_deepening_search(graph, start, goal)
if result:
    print("Path found:", " -> ".join(result))
else:
    print("Goal not found")
