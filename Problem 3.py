import random

def randomized_hill_climbing(objective_function, initial_state, neighbor_function, max_iterations=1000):
    current_state = initial_state
    current_value = objective_function(current_state)
    
    for _ in range(max_iterations):
        neighbor = neighbor_function(current_state)
        neighbor_value = objective_function(neighbor)
        
        if neighbor_value > current_value:  # For maximization
            current_state = neighbor
            current_value = neighbor_value
    
    return current_state, current_value

# Test functions
def minimization_function(x):
    return (x - 3) ** 2

def maximization_function(x):
    return -x**2 + 5

# Neighbor function for integer optimization
def integer_neighbor(x):
    return x + random.choice([-1, 1])

# Test RHC on simple functions
print("Testing RHC on simple functions:")
min_result = randomized_hill_climbing(lambda x: -minimization_function(x), 0, integer_neighbor)
max_result = randomized_hill_climbing(maximization_function, 0, integer_neighbor)

print(f"Minimization result: x = {min_result[0]}, f(x) = {minimization_function(min_result[0])}")
print(f"Maximization result: x = {max_result[0]}, f(x) = {max_result[1]}")

# Resource Allocation Problem
class Project:
    def __init__(self, id, resource_requirement, benefit):
        self.id = id
        self.resource_requirement = resource_requirement
        self.benefit = benefit

def allocate_resources(projects, total_resources, maximize=True):
    def objective_function(allocation):
        total_benefit = sum(projects[i].benefit for i, alloc in enumerate(allocation) if alloc)
        total_resources_used = sum(projects[i].resource_requirement for i, alloc in enumerate(allocation) if alloc)
        if total_resources_used > total_resources:
            return -float('inf') if maximize else float('inf')
        return total_benefit if maximize else -total_benefit

    def neighbor_function(allocation):
        new_allocation = allocation.copy()
        index = random.randint(0, len(allocation) - 1)
        new_allocation[index] = not new_allocation[index]
        return new_allocation

    initial_state = [False] * len(projects)
    best_allocation, best_value = randomized_hill_climbing(objective_function, initial_state, neighbor_function)
    
    return best_allocation, abs(best_value)

# Test cases
test_case_1 = [
    Project("1", 20, 40),
    Project("2", 30, 50),
    Project("3", 25, 30),
    Project("4", 15, 25)
]

test_case_2 = [
    Project("A", 10, 15),
    Project("B", 40, 60),
    Project("C", 20, 30),
    Project("D", 25, 35),
    Project("E", 5, 10)
]

test_case_3 = [
    Project("X", 50, 80),
    Project("Y", 30, 45),
    Project("Z", 15, 20),
    Project("W", 25, 35)
]

# Run test cases
print("\nTest Case 1 (Maximize benefit):")
allocation_1, total_benefit_1 = allocate_resources(test_case_1, 100, maximize=True)
print(f"Allocation: {[p.id for i, p in enumerate(test_case_1) if allocation_1[i]]}")
print(f"Total Benefit: {total_benefit_1}")

print("\nTest Case 2 (Minimize time):")
allocation_2, total_time_2 = allocate_resources(test_case_2, 100, maximize=False)
print(f"Allocation: {[p.id for i, p in enumerate(test_case_2) if allocation_2[i]]}")
print(f"Total Time: {total_time_2}")

print("\nTest Case 3 (Maximize benefit):")
allocation_3, total_benefit_3 = allocate_resources(test_case_3, 100, maximize=True)
print(f"Allocation: {[p.id for i, p in enumerate(test_case_3) if allocation_3[i]]}")
print(f"Total Benefit: {total_benefit_3}")