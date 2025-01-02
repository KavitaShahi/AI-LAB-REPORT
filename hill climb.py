class PuzzleState:
    def __init__(self, board, parent=None):
        self.board = board  # Current state of the puzzle
        self.parent = parent  # Parent state (to trace the path)
        self.h = self.calculate_heuristic()  # Heuristic value (Manhattan Distance)

    def calculate_heuristic(self):
        """Calculate Manhattan distance for the current board configuration."""
        distance = 0
        goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)
        for i, tile in enumerate(self.board):
            if tile != 0:  # Ignore the blank space
                goal_x, goal_y = divmod(tile - 1, 3)
                current_x, current_y = divmod(i, 3)
                distance += abs(goal_x - current_x) + abs(goal_y - current_y)
        return distance

    def generate_successors(self):
        """Generate all valid successor states by moving the blank space."""
        blank_pos = self.board.index(0)
        blank_x, blank_y = divmod(blank_pos, 3)
        successors = []
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

        for dx, dy in moves:
            new_x, new_y = blank_x + dx, blank_y + dy
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                # Valid move, generate new board configuration
                new_blank_pos = new_x * 3 + new_y
                new_board = list(self.board)
                # Swap blank space with the tile in the new position
                new_board[blank_pos], new_board[new_blank_pos] = new_board[new_blank_pos], new_board[blank_pos]
                successors.append(PuzzleState(tuple(new_board), self))

        return successors

def steepest_ascent_hill_climbing(start_state):
    """Perform Steepest Ascent Hill Climbing for the 8-puzzle problem."""
    current_state = start_state

    while current_state.h > 0:
        # Generate all possible successors
        successors = current_state.generate_successors()

        # Find the successor with the minimum heuristic value (closest to goal)
        best_successor = None
        for successor in successors:
            if best_successor is None or successor.h < best_successor.h:
                best_successor = successor

        # If no better successor is found, the search has reached a local maximum
        if best_successor.h >= current_state.h:
            print("No solution found (local maximum reached).")
            return None

        # Move to the best successor
        current_state = best_successor
        print(current_state.board)

    # Reached goal state
    print("Goal reached!")
    return current_state

# Test the Steepest Ascent Hill Climbing on the 8-puzzle problem
if __name__ == "__main__":
    start_board = (2, 8, 3, 1, 6, 4, 7, 0, 5)  # Random start state
    start_state = PuzzleState(start_board)

    # Solve the puzzle using Steepest Ascent Hill Climbing
    solution = steepest_ascent_hill_climbing(start_state)

    if solution:
        print("Solution path:")
        path = []
        while solution:
            path.append(solution.board)
            solution = solution.parent
        path.reverse()
        for step in path:
            print(step[:3])
            print(step[3:6])
            print(step[6:])
            print()
