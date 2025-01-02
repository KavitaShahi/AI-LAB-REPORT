class WaterJug:
    def __init__(self, capacity_4, capacity_3, initial_state, goal_state):
        self.capacity_4 = capacity_4
        self.capacity_3 = capacity_3
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.visited = set()  # Set to keep track of visited states
        self.parent = {}  # Dictionary to track parent state for path generation

    def goal_test(self, current_state):
        """Check if current state is the goal state."""
        return current_state == self.goal_state

    def successor(self, current_state):
        """Generate possible successor states based on the problem's actions."""
        successors = []
        x, y = current_state
        
        # Fill the 3-liter jug
        if y < self.capacity_3:
            successors.append((x, self.capacity_3))
        
        # Fill the 4-liter jug
        if x < self.capacity_4:
            successors.append((self.capacity_4, y))
        
        # Empty the 3-liter jug
        if y > 0:
            successors.append((x, 0))
        
        # Empty the 4-liter jug
        if x > 0:
            successors.append((0, y))
        
        # Pour water from the 3-liter jug into the 4-liter jug
        if x < self.capacity_4 and y > 0:
            pour = min(self.capacity_4 - x, y)
            successors.append((x + pour, y - pour))
        
        # Pour water from the 4-liter jug into the 3-liter jug
        if y < self.capacity_3 and x > 0:
            pour = min(self.capacity_3 - y, x)
            successors.append((x - pour, y + pour))
        
        return successors

    def dfs(self):
        """Depth-First Search (DFS) algorithm to solve the water jug problem."""
        stack = [self.initial_state]
        self.visited.add(self.initial_state)
        self.parent[self.initial_state] = None  # Starting state has no parent

        while stack:
            current_state = stack.pop()
            if self.goal_test(current_state):
                return self.generate_path(current_state)
            
            # Explore successors
            for next_state in self.successor(current_state):
                if next_state not in self.visited:
                    self.visited.add(next_state)
                    self.parent[next_state] = current_state
                    stack.append(next_state)

        return None  # Return None if no solution is found

    def generate_path(self, goal_state):
        """Generate the path from the initial state to the goal state."""
        path = []
        current_state = goal_state
        while current_state is not None:
            path.append(current_state)
            current_state = self.parent[current_state]
        return path[::-1]  # Reverse the path to get from initial to goal


# Test the WaterJug class with DFS
if __name__ == "__main__":
    initial_state = (4, 0)  # 4-liter jug filled with 4 liters, 3-liter jug is empty
    goal_state = (2, 0)     # Goal is to have exactly 2 liters in the 4-liter jug
    
    water_jug = WaterJug(4, 3, initial_state, goal_state)
    solution_path = water_jug.dfs()

    if solution_path:
        print("Solution found:")
        for state in solution_path:
            print(state)
    else:
        print("No solution found.")
