import heapq

# Goal state for the 8-puzzle problem
goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)

# Directions for moving the blank space (up, down, left, right)
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

class PuzzleState:
    def __init__(self, board, parent=None, g=0):
        self.board = board  # Current state of the puzzle
        self.parent = parent  # Parent state
        self.g = g  # Cost to reach the current state (number of moves)
        self.h = self.calculate_heuristic()  # Heuristic value (Manhattan Distance)
        self.f = self.g + self.h  # Total estimated cost

    def calculate_heuristic(self):
        """Calculate Manhattan distance for the current board configuration."""
        distance = 0
        for i, tile in enumerate(self.board):
            if tile != 0:  # Ignore the blank space
                goal_x, goal_y = divmod(tile - 1, 3)
                current_x, current_y = divmod(i, 3)
                distance += abs(goal_x - current_x) + abs(goal_y - current_y)
        return distance

    def __lt__(self, other):
        """Define the less than comparison for the priority queue."""
        return self.f < other.f

    def generate_successors(self):
        """Generate all valid successor states by moving the blank space."""
        blank_pos = self.board.index(0)
        blank_x, blank_y = divmod(blank_pos, 3)
        successors = []

        for dx, dy in moves:
            new_x, new_y = blank_x + dx, blank_y + dy
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                # Valid move, generate new board configuration
                new_blank_pos = new_x * 3 + new_y
                new_board = list(self.board)
                # Swap blank space with the tile in the new position
                new_board[blank_pos], new_board[new_blank_pos] = new_board[new_blank_pos], new_board[blank_pos]
                successors.append(PuzzleState(tuple(new_board), self, self.g + 1))

        return successors

def a_star(start_state):
    """Perform A* search algorithm to solve the 8-puzzle problem."""
    open_list = []
    closed_set = set()

    # Push the initial state onto the priority queue
    heapq.heappush(open_list, start_state)
    
    while open_list:
        # Pop the state with the lowest f-value
        current_state = heapq.heappop(open_list)
        
        # If we reached the goal state, reconstruct the path
        if current_state.board == goal_state:
            path = []
            while current_state:
                path.append(current_state.board)
                current_state = current_state.parent
            return path[::-1]  # Return the path from start to goal

        # Add the current state to the closed set
        closed_set.add(current_state.board)

        # Generate and evaluate successors
        for successor in current_state.generate_successors():
            if successor.board not in closed_set:
                heapq.heappush(open_list, successor)

    return None  # No solution found

# Test the A* algorithm on the 8-puzzle problem
if __name__ == "__main__":
    start_board = (2, 8, 3, 1, 6, 4, 7, 0, 5)  # A random start state for the puzzle
    start_state = PuzzleState(start_board)
    
    # Solve the puzzle using A* algorithm
    solution = a_star(start_state)
    
    if solution:
        print("Solution found!")
        for step in solution:
            print(step[:3])
            print(step[3:6])
            print(step[6:])
            print()
    else:
        print("No solution found.")
