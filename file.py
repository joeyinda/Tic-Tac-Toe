import random

# Function to print the Tic-Tac-Toe board
def print_board(board):
    print("---------")
    for row in board:
        print("|", end=" ")
        for cell in row:
            print(cell, end=" ")
        print("|")
    print("---------")

# Function to check if a player has won
def check_win(board, player):
    # Check rows
    for row in board:
        if row.count(player) == 3:
            return True

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

# Function to make a player's move
def make_move(board, player):
    while True:
        row = int(input("Enter the row (0-2): "))
        col = int(input("Enter the column (0-2): "))

        if board[row][col] == " ":
            board[row][col] = player
            break
        else:
            print("Invalid move. Try again.")

# Function to make the computer's move
def make_computer_move(board, computer, player):
    print("Computer's turn...")
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)

        if board[row][col] == " ":
            board[row][col] = computer
            break

# Main game loop
def play_game():
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    players = ["X", "O"]
    current_player = random.choice(players)

    print("Welcome to Tic-Tac-Toe!")
    print("You are playing as", current_player)
    print_board(board)

    while True:
        if current_player == "X":
            make_move(board, current_player)
        else:
            make_computer_move(board, current_player, players)

        print_board(board)

        if check_win(board, current_player):
            print(current_player, "wins!")
            break
        elif " " not in [cell for row in board for cell in row]:
            print("It's a tie!")
            break

        current_player = players[1] if current_player == players[0] else players[0]

# Start the game
play_game()
