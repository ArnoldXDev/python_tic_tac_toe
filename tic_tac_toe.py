# tic_tac_toe.py
# ===================
# A simple 2-player Tic-Tac-Toe game implemented in Python.
# This game allows two players to take turns marking spaces on a 3x3 grid.
# The first player to align three marks in a row, column, or diagonal wins.
#
# Features:
# - Player 1 uses "X" and Player 2 uses "O".
# - Input validation to ensure players select valid rows and columns.
# - Game announces the winner once a player wins.
#
# How to Run:
# 1. Make sure you have Python installed.
# 2. Run this file in your terminal or command prompt using:
#    python tic_tac_toe.py
#
# Enjoy playing!

def print_board(board):
    # Print top border of the board
    print("\n" + "-" * 13)  # The 13 dashes make the top border with space for the cells
    for row in board:
        # Print each row with borders around the cells
        print(f"| {row[0]} | {row[1]} | {row[2]} |")  # Format each cell of the row with vertical borders
        # Print separator between rows
        print("-" * 13)  # Creates a line to separate rows of the board

def check_winner(board):
    # Check for a winner in rows, columns, and diagonals
    for row in board:
        # Check if all three cells in the row are the same and not empty
        if row[0] == row[1] == row[2] != " ":
            return row[0]  # Return the player ('X' or 'O') who won

    for col in range(3):
        # Check if all three cells in the column are the same and not empty
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]  # Return the player ('X' or 'O') who won

    # Check the diagonal from top-left to bottom-right
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]  # Return the player ('X' or 'O') who won

    # Check the diagonal from top-right to bottom-left
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]  # Return the player ('X' or 'O') who won

    return None  # No winner yet

def tic_tac_toe():
    # Initialize an empty board with spaces
    board = [[" " for _ in range(3)] for _ in range(3)]
    # Start the game with Player 'X'
    current_player = "X"

    while True:
        print_board(board)  # Display the current state of the board
        
        try:
            # Get the row and column from the current player
            row = int(input(f"Player {current_player}, enter the row (0-2): "))
            col = int(input(f"Player {current_player}, enter the column (0-2): "))
            
            # Check if the selected cell is empty
            if board[row][col] == " ":
                board[row][col] = current_player  # Mark the cell with the current player's symbol
            else:
                print("Cell is already occupied. Try again.")  # If the cell is occupied, prompt the player to choose again
                continue
        except (ValueError, IndexError):
            # Handle invalid input (non-integer or out of range)
            print("Invalid input. Please enter a valid row and column (0-2).")
            continue
        
        winner = check_winner(board)  # Check if there is a winner
        
        if winner:
            print_board(board)  # Display the final board with the winning move
            print(f"Player {winner} wins!")  # Announce the winner
            break  # End the game

        # Switch players after each turn
        current_player = "O" if current_player == "X" else "X"

# Start the Tic-Tac-Toe game
tic_tac_toe()
