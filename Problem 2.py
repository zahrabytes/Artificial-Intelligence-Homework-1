import math
import heapq

def euclidean_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    dx = x2 - x1
    dy = y2 - y1
    return math.sqrt(dx**2 + dy**2)

def a_star(graph, start, goal):
    open_set = [(0, start, [])]
    closed_set = set()
    g_costs = {start: 0}
    
    while open_set:
        f_cost, current, path = heapq.heappop(open_set)
        if current == goal:
            return path + [current]
        if current in closed_set:
            continue
        closed_set.add(current)
        for neighbor, edge_cost in graph[current]:
            if neighbor in closed_set:
                continue
            tentative_g = g_costs[current] + edge_cost
            if neighbor not in g_costs or tentative_g < g_costs[neighbor]:
                g_costs[neighbor] = tentative_g
                h_cost = euclidean_distance(neighbor, goal)
                f_cost = tentative_g + h_cost
                new_path = path + [current]
                heapq.heappush(open_set, (f_cost, neighbor, new_path))
    
    return None  # no path found

#I used the one from the example
graph = {
    (0,0): [((1,0), 4), ((0,1), 2)],
    (1,0): [((0,0), 4), ((2,0), 3), ((1,1), 1)],
    (2,0): [((1,0), 3), ((2,1), 4)],
    (0,1): [((0,0), 2), ((0,2), 3), ((1,1), 3)],
    (1,1): [((0,1), 3), ((1,0), 1), ((1,2), 2), ((2,1), 4)],
    (2,1): [((2,0), 4), ((1,1), 4), ((2,2), 5)],
    (0,2): [((0,1), 3), ((1,2), 7)],
    (1,2): [((0,2), 7), ((1,1), 2), ((2,2), 1)],
    (2,2): [((1,2), 1), ((2,1), 5), ((2,3), 3)],
    (2,3): [((2,2), 3)]
}

#credit: asked claude ai to give me different traffic scenarios. even then it didnt change that much

graph_increased = {
    (0,0): [((1,0), 20), ((0,1), 18)],  # drastically increased both
    (1,0): [((0,0), 20), ((2,0), 15), ((1,1), 12)],  # increased all
    (2,0): [((1,0), 15), ((2,1), 14)],  # increased both
    (0,1): [((0,0), 18), ((0,2), 13), ((1,1), 17)],  # increased all
    (1,1): [((0,1), 17), ((1,0), 12), ((1,2), 15), ((2,1), 14)],  # increased all
    (2,1): [((2,0), 14), ((1,1), 14), ((2,2), 20)],  # increased all
    (0,2): [((0,1), 13), ((1,2), 17)],  # increased both
    (1,2): [((0,2), 17), ((1,1), 15), ((2,2), 13)],  # increased all
    (2,2): [((1,2), 13), ((2,1), 20), ((2,3), 16)],  # increased all
    (2,3): [((2,2), 16)]  # increased
}

graph_decreased = {
    (0,0): [((1,0), 1), ((0,1), 3)],  # created a "superhighway" to (1,0)
    (1,0): [((0,0), 1), ((2,0), 1), ((1,1), 2)],  # "superhighway" continues to (2,0)
    (2,0): [((1,0), 1), ((2,1), 1)],  # "superhighway" to (2,1)
    (0,1): [((0,0), 3), ((0,2), 2), ((1,1), 3)],
    (1,1): [((0,1), 3), ((1,0), 2), ((1,2), 2), ((2,1), 2)],
    (2,1): [((2,0), 1), ((1,1), 2), ((2,2), 1)],  # "superhighway" continues to (2,2)
    (0,2): [((0,1), 2), ((1,2), 3)],
    (1,2): [((0,2), 3), ((1,1), 2), ((2,2), 2)],
    (2,2): [((1,2), 2), ((2,1), 1), ((2,3), 1)],  # "superhighway" ends at (2,3)
    (2,3): [((2,2), 1)]
}

graph_mixed = {
    (0,0): [((1,0), 10), ((0,1), 1)],  # Created a "fast lane" to (0,1) but blocked (1,0)
    (1,0): [((0,0), 10), ((2,0), 1), ((1,1), 8)],  # Fast lane to (2,0), blocked others
    (2,0): [((1,0), 1), ((2,1), 10)],  # Fast from (1,0), but blocked to (2,1)
    (0,1): [((0,0), 1), ((0,2), 10), ((1,1), 1)],  # Fast lane continues to (1,1)
    (1,1): [((0,1), 1), ((1,0), 8), ((1,2), 1), ((2,1), 8)],  # Fast to (1,2), others slow
    (2,1): [((2,0), 10), ((1,1), 8), ((2,2), 1)],  # Fast lane to (2,2)
    (0,2): [((0,1), 10), ((1,2), 10)],  # Both paths blocked
    (1,2): [((0,2), 10), ((1,1), 1), ((2,2), 10)],  # Fast from (1,1), others blocked
    (2,2): [((1,2), 10), ((2,1), 1), ((2,3), 1)],  # Fast lane continues to goal
    (2,3): [((2,2), 1)]  # Fast final step
}

#"The warehouse is at (0, 0) and the customer's home is at (2, 3)."

start = (0,0)
goal = (2,3)

# using the original graph
path = a_star(graph, start, goal)
print("path (original graph):", path)

# now with lots of traffic
path_increased = a_star(graph_increased, start, goal)
print("path (with some traffic):", path_increased)

# with the diet version (less traffic)
path_decreased = a_star(graph_decreased, start, goal)
print("path (light edition):", path_decreased)

# with the mixed version (very diverse!)
path_mixed = a_star(graph_mixed, start, goal)
print("path (diverse edition):", path_mixed)

def path_cost(graph, path):
    return sum(next(cost for node, cost in graph[path[i]] if node == path[i+1]) for i in range(len(path)-1))

# Define scenarios
scenarios = {
    "Normal Traffic": graph,
    "Heavy Traffic": graph_increased,
    "Light Traffic": graph_decreased,
    "Mixed Traffic": graph_mixed
}

results = {}

for scenario, g in scenarios.items():
    path = a_star(g, start, goal)
    travel_time = path_cost(g, path)
    results[scenario] = {"path": path, "travel_time": travel_time}

# Print results
print("Optimal Paths and Travel Times:")
print("---------------------------------")
for scenario, data in results.items():
    print(f"{scenario}:")
    print(f"  Path: {' -> '.join(map(str, data['path']))}")
    print(f"  Travel Time: {data['travel_time']} units")
    print()

# Visualize the paths
def visualize_paths(results):
    for scenario, data in results.items():
        path = data['path']
        print(f"\n{scenario} Path:")
        for y in range(4):  # Extended to 4 to include the goal at (2,3)
            for x in range(3):
                if (x, y) in path:
                    print("O", end=" ")
                else:
                    print(".", end=" ")
            print()

visualize_paths(results)