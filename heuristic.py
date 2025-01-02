def calculate_heuristic(start, goal):
    """
    Calculate the heuristic value for the Blocks World problem.
    
    :param start: List representing the current state (e.g., ['A', 'D', 'C', 'B']).
    :param goal: List representing the goal state (e.g., ['D', 'C', 'B', 'A']).
    :return: Heuristic value (int).
    """
    heuristic = 0
    for i in range(len(start)):
        # Check if the block is in the correct position
        if start[i:] == goal[i:]:
            heuristic += len(start) - i
            break
        elif start[i] == goal[i]:
            heuristic += 1
        else:
            heuristic -= 1
    return heuristic


# Example usage
start_state = ['A', 'D', 'C', 'B']
goal_state = ['D', 'C', 'B', 'A']
heuristic_value = calculate_heuristic(start_state, goal_state)
print(f"Heuristic value: {heuristic_value}")