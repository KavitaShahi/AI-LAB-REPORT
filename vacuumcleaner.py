import random

# Define the grid size
GRID_SIZE = 4  # 4x4 grid for simplicity

# Define the environment
class Environment:
    def __init__(self):
        # Initialize a grid with random dirty or clean states
        self.grid = [[random.choice(['clean', 'dirty']) for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        self.agent_position = (0, 0)  # Initial position of the agent

    def is_dirty(self, x, y):
        """Check if the room at (x, y) is dirty."""
        return self.grid[x][y] == 'dirty'

    def clean(self, x, y):
        """Clean the room at (x, y)."""
        self.grid[x][y] = 'clean'

    def print_grid(self):
        """Print the current state of the grid."""
        for row in self.grid:
            print(" ".join(row))
        print()

# Define the vacuum cleaner agent
class ReflexVacuumAgent:
    def __init__(self, environment):
        self.environment = environment
        self.position = environment.agent_position  # Start at (0, 0)

    def sense_and_act(self):
        """Sense the environment and act accordingly."""
        x, y = self.position
        # If the current room is dirty, clean it
        if self.environment.is_dirty(x, y):
            print(f"Room ({x}, {y}) is dirty. Cleaning it.")
            self.environment.clean(x, y)
        else:
            print(f"Room ({x}, {y}) is clean. Moving.")
            self.move()

    def move(self):
        """Move to a random adjacent room."""
        x, y = self.position
        possible_moves = []
        
        # Check valid adjacent rooms
        if x > 0: possible_moves.append((x - 1, y))  # Up
        if x < GRID_SIZE - 1: possible_moves.append((x + 1, y))  # Down
        if y > 0: possible_moves.append((x, y - 1))  # Left
        if y < GRID_SIZE - 1: possible_moves.append((x, y + 1))  # Right
        
        # Choose a random valid move
        self.position = random.choice(possible_moves)

    def run(self, steps=10):
        """Run the vacuum cleaner agent for a number of steps."""
        for _ in range(steps):
            self.environment.print_grid()
            self.sense_and_act()

# Create the environment and 
