import heapq

def heuristic(node, goal):
    """Estimate the cost from node to goal using Manhattan distance."""
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

def astar_search(graph, start, goal):
    """
    Find the shortest path from start to goal using the A* search algorithm.

    graph: dict mapping each node to a list of (neighbor, cost) tuples
    start: starting node
    goal:  target node

    Returns the shortest path as a list of nodes, or None if no path exists.
    """
    open_set = []
    heapq.heappush(open_set, (0, start))

    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}

    while open_set:
        current_f, current_node = heapq.heappop(open_set)

        if current_node == goal:
            return reconstruct_path(came_from, current_node)

        for neighbor, edge_cost in graph.get(current_node, []):
            tentative_g = g_score[current_node] + edge_cost

            if tentative_g < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current_node
                g_score[neighbor] = tentative_g
                f_score[neighbor] = tentative_g + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None  # No path found

def reconstruct_path(came_from, current_node):
    """Rebuild the path by following came_from pointers back to the start."""
    path = [current_node]
    while current_node in came_from:
        current_node = came_from[current_node]
        path.append(current_node)
    path.reverse()
    return path
