import time

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
 
    for i in range(3):
        if all([cell == player for cell in board[i]]) or all([board[j][i] == player for j in range(3)]):
            return True
    if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def knots_and_crosses():
    print("Welcome to Knots and Crosses (Tic-Tac-Toe)!")
    print("Get ready for an exciting game between Player X and Player O!\n")
    time.sleep(1)
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0

    while True:
        print_board(board)
        print(f"Player {players[current_player]}'s turn.")
        try:
            row = int(input("Enter the row (0, 1, 2): "))
            col = int(input("Enter the column (0, 1, 2): "))
            if board[row][col] != " ":
                print("\nOops! Cell already taken. Try again.\n")
                continue
        except (ValueError, IndexError):
            print("\nInvalid input! Please enter a valid row and column (0, 1, 2).\n")
            continue

        board[row][col] = players[current_player]
        print("\nNice move! Let's see what happens next...\n")
        time.sleep(1)

        if check_winner(board, players[current_player]):
            print_board(board)
            print(f"\nCongratulations! Player {players[current_player]} wins! 🎉")
            break
        elif is_full(board):
            print_board(board)
            print("\nIt's a draw! Well played both! 🤝")
            break

        current_player = 1 - current_player
        print("\nSwitching turns...\n")
        time.sleep(1)


knots_and_crosses()
