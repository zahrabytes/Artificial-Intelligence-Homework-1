from collections import deque
import math #for inf

def findMinDistanceVertex(Q, dist):
    minimum = math.inf
    min_vertex = None
    for vertex in Q:
        if dist[vertex] < minimum:
            minumim = dist[vertex]
            min_vertex = vertex
    return min_vertex

def printPaths(find_these, distances, prev):
    for vertex in find_these:
        path = []
        current = vertex
        while current is not None:
            path.append(current)
            current = prev[current]
        path.reverse()
        path_str = ' -> '.join(map(str, path))
        print(f"To vertex {vertex}: {path_str:<30} Weight: {distances[vertex]:<6}")

def dijkstras(graph): # for BFS
    Q = deque(graph.keys()) #vertices to visit
    distances = {vertex: math.inf for vertex in graph} #distances from origin
    distances[0] = 0
    prev = {vertex: None for vertex in graph} # previously visited with vertex visited 

    #visit one vertex

    while Q:
        min_vertex = findMinDistanceVertex(Q, distances)
        Q.remove(min_vertex)
        for neighbor, weight in graph[min_vertex]:
            if distances[min_vertex] == math.inf:
                distance = weight
            else:
                distance = distances[min_vertex] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                prev[neighbor] = min_vertex
    return prev, distances

def depth_first_shortest_path(graph, start, targets):
    def dfs(vertex, path, weight):
        if weight >= distances[vertex]:
            return  # Prune if we've found a shorter path already

        distances[vertex] = weight
        prev[vertex] = path[-2] if len(path) > 1 else None

        if vertex in targets and all(distances[t] != math.inf for t in targets):
            return  # Early termination if all targets are found

        for neighbor, edge_weight in graph[vertex]:
            dfs(neighbor, path + [neighbor], weight + edge_weight)

    distances = {vertex: math.inf for vertex in graph}
    prev = {vertex: None for vertex in graph}
    
    dfs(start, [start], 0)
    
    return prev, distances

graph = {
    0: [(1, 2), (7, 3), (3, 2)],  
    1: [(0, 1), (4, 4)],  
    3: [(0, 1), (5, 7)],
    4: [(6, 4)],
    5: [(6, 2)],
    6: [],
    7: [(4, 5), (5, 6)]
}
max_vertex = max(graph.keys())
find_these = [5, 6, 7]
Dijkstras_prev, Dijkstras_distances = dijkstras(graph)
DFS_prev, DFS_distances = depth_first_shortest_path(graph, 0, find_these)
print("Shortest paths and weights:")
print("BFS")
printPaths(find_these, Dijkstras_distances, Dijkstras_prev)
print("DFS")
printPaths(find_these, DFS_distances, DFS_prev)
