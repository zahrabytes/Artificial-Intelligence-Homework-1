import random

class Project:
    def __init__(self, id, resource_requirement, value):
        self.id = id
        self.resource_requirement = resource_requirement
        self.value = value

def randomized_hill_climbing(projects, total_resources, maximize=True, max_iterations=1000): 
    def objective_function(allocation):#Claude Ai helped me for this part
        total_value = sum(projects[i].value for i, alloc in enumerate(allocation) if alloc)
        total_resources_used = sum(projects[i].resource_requirement for i, alloc in enumerate(allocation) if alloc)
        if total_resources_used > total_resources:
            return -float('inf') if maximize else float('inf')
        return total_value if maximize else -total_value

    def neighbor_function(allocation):
        new_allocation = allocation.copy()
        index = random.randint(0, len(allocation) - 1)
        new_allocation[index] = not new_allocation[index]
        return new_allocation

    current_allocation = [False] * len(projects)
    current_value = objective_function(current_allocation)

    for _ in range(max_iterations):
        neighbor = neighbor_function(current_allocation)
        neighbor_value = objective_function(neighbor)
        
        if (maximize and neighbor_value > current_value) or (not maximize and neighbor_value < current_value):
            current_allocation = neighbor
            current_value = neighbor_value

    return current_allocation, abs(current_value)

projects_1 = [
    Project("1", 20, 40),
    Project("2", 30, 50),
    Project("3", 25, 30),
    Project("4", 15, 25)
]

projects_2 = [
    Project("A", 10, 15),
    Project("B", 40, 60),
    Project("C", 20, 30),
    Project("D", 25, 35),
    Project("E", 5, 10)
]

projects_3 = [
    Project("X", 50, 80),
    Project("Y", 30, 45),
    Project("Z", 15, 20),
    Project("W", 25, 35)
]

def solve_and_print(projects, total_resources, maximize, case_num):
    allocation, total_value = randomized_hill_climbing(projects, total_resources, maximize)
    selected_projects = [p.id for i, p in enumerate(projects) if allocation[i]]
    resources_used = sum(p.resource_requirement for i, p in enumerate(projects) if allocation[i])
    
    print(f"\nTest Case {case_num}:")
    print(f"Selected Projects: {selected_projects}")
    print(f"Total {'Benefit' if maximize else 'Time'}: {total_value}")
    print(f"Resources Used: {resources_used}/{total_resources}")

solve_and_print(projects_1, 100, True, 1)   # Maximize benefit
solve_and_print(projects_2, 100, False, 2)  # Minimize time
solve_and_print(projects_3, 100, True, 3)   # Maximize benefit