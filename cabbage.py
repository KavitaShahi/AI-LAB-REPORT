from collections import deque

class ManGoatLionCabbage:
    def __init__(self):
        # Initial state is (0, 0, 0, 0) and goal state is (1, 1, 1, 1)
        self.initial_state = (0, 0, 0, 0)
        self.goal_state = (1, 1, 1, 1)
    
    def is_valid_state(self, state):
        """Check if a state is valid according to the rules."""
        man, goat, lion, cabbage = state
        # Check if the goat is left with the cabbage without the man, or if the lion is left with the goat without the man
        if (goat == cabbage and man != goat) or (lion == goat and man != lion):
            return False
        return True

    def get_successors(self, state):
        """Generate all valid successor states."""
        man, goat, lion, cabbage = state
        successors = []
        
        # The man can take one item across or just cross alone
        possible_moves = [(man, goat, lion, cabbage),  # Man crosses alone
                          (1 - man, 1 - goat, lion, cabbage),  # Man takes goat
                          (1 - man, goat, 1 - lion, cabbage),  # Man takes lion
                          (1 - man, goat, lion, 1 - cabbage)]  # Man takes cabbage
        
        for move in possible_moves:
            if self.is_valid_state(move):
                successors.append(move)
        
        return successors

    def bfs(self):
        """Perform BFS to find the shortest path to the goal state."""
        queue = deque([(self.initial_state, [])])  # queue contains tuples of (state, path)
        visited = set()
        visited.add(self.initial_state)

        while queue:
            current_state, path = queue.popleft()

            # If we reached the goal state, return the path
            if current_state == self.goal_state:
                return path + [current_state]

            # Get the successors and add them to the queue if not visited
            for successor in self.get_successors(current_state):
                if successor not in visited:
                    visited.add(successor)
                    queue.append((successor, path + [current_state]))

        return None  # No solution found

    def print_solution(self):
        """Print the solution path."""
        solution_path = self.bfs()
        if solution_path:
            print("Solution Path:")
            for step in solution_path:
                print(step)
        else:
            print("No solution found.")

# Instantiate and solve the problem
if __name__ == "__main__":
    puzzle = ManGoatLionCabbage()
    puzzle.print_solution()
