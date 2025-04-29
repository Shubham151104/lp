import heapq

def prims_algorithm(graph, start_node):
    visited = set()
    min_heap = [(0, start_node)]  # (weight, node)
    total_cost = 0

    while min_heap:
        weight, current_node = heapq.heappop(min_heap)
        if current_node in visited:
            continue
        visited.add(current_node)
        total_cost += weight
        print(f"Visited {current_node} with edge weight {weight}")

        for neighbor, edge_weight in graph[current_node]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (edge_weight, neighbor))

    print(f"Total cost of Minimum Spanning Tree: {total_cost}")

# Example graph as adjacency list
graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 1), ('D', 1)],
    'C': [('A', 3), ('B', 1), ('D', 4)],
    'D': [('B', 1), ('C', 4)]
}

prims_algorithm(graph, 'A')
