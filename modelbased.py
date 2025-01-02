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

# Define the model-based vacuum cleaner agent
class ModelBasedVacuumAgent:
    def __init__(self, environment):
        self.environment = environment
        self.position = environment.agent_position  # Start at (0, 0)
        self.memory = [[None for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]  # Memory of the environment
        self.memory[self.position[0]][self.position[1]] = 'dirty' if environment.is_dirty(self.position[0], self.position[1]) else 'clean'

    def sense_and_act(self):
        """Sense the environment and act accordingly."""
        x, y = self.position
        # Sense the current room
        current_room_state = self.memory[x][y]

        # If the current room is dirty, clean it
        if current_room_state == 'dirty':
            print(f"Room ({x}, {y}) is dirty. Cleaning it.")
            self.environment.clean(x, y)
            self.memory[x][y] = 'clean'
        else:
            print(f"Room ({x}, {y}) is clean. Moving to the next unclean room.")
            self.move()

    def move(self):
        """Move to an adjacent room based on the memory of the environment."""
        x, y = self.position
        possible_moves = []

        # Check valid adjacent rooms
        if x > 0 and self.memory[x - 1][y] != 'clean': possible_moves.append((x - 1, y))  # Up
        if x < GRID_SIZE - 1 and self.memory[x + 1][y] != 'clean': possible_moves.append((x + 1, y))  # Down
        if y > 0 and self.memory[x][y - 1] != 'clean': possible_moves.append((x, y - 1))  # Left
        if y < GRID_SIZE - 1 and self.memory[x][y + 1] != 'clean': possible_moves.append((x, y + 1))  # Right
        
        # If there are valid moves, choose the best move (we're prioritizing the first unclean room)
        if possible_moves:
            self.position = random.choice(possible_moves)
            self.memory[self.position[0]][self.position[1]] = 'dirty' if self.environment.is_dirty(self.position[0], self.position[1]) else 'clean'

    def run(self, steps=10):
        """Run the vacuum cleaner agent for a number of steps."""
        for _ in range(steps):
            self.environment.print_grid()
            self.sense_and_act()

# Create the environment and agent
env = Environment()
agent = ModelBasedVacuumAgent(env)

# Run the agent for 10 steps
agent.run(steps=10)
