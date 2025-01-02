def calculate_heuristic(board, player, opponent):
    """
    Calculate the heuristic value for a given Tic-Tac-Toe board state.

    Parameters:
        board: 2D list representing the Tic-Tac-Toe board (3x3).
        player: Character representing the current player ('X' or 'O').
        opponent: Character representing the opponent ('X' or 'O').

    Returns:
        Heuristic value (integer).
    """
    def is_open_line(line, current_player):
        # A line is open if it has no opponent marks and at least one empty cell
        return all(cell == current_player or cell == ' ' for cell in line)
    
    def count_open_lines(current_player):
        open_lines = 0
        
        # Check rows
        for row in board:
            if is_open_line(row, current_player):
                open_lines += 1

        # Check columns
        for col in range(3):
            column = [board[row][col] for row in range(3)]
            if is_open_line(column, current_player):
                open_lines += 1

        # Check diagonals
        diagonal1 = [board[i][i] for i in range(3)]
        diagonal2 = [board[i][2 - i] for i in range(3)]
        if is_open_line(diagonal1, current_player):
            open_lines += 1
        if is_open_line(diagonal2, current_player):
            open_lines += 1

        return open_lines

    player_open_lines = count_open_lines(player)
    opponent_open_lines = count_open_lines(opponent)

    return player_open_lines - opponent_open_lines


# Example usage
tic_tac_toe_board = [
    ['X', ' ', ' '],
    [' ', 'O', ' '],
    [' ', ' ', ' ']
]
player = 'X'
opponent = 'O'

heuristic_value = calculate_heuristic(tic_tac_toe_board, player, opponent)
print("Heuristic value:", heuristic_value)