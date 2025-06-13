# Tic Tac Toe Game - 2 Player Console Version

def print_board(board):
    print()
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:
            print("-" * 9)
    print()

def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def show_board_guide():
    print("Board Coordinates:")
    print("  0   1   2")
    print("0 _ | _ | _")
    print("1 _ | _ | _")
    print("2 _ | _ | _")
    print()

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    show_board_guide()

    while True:
        print_board(board)
        try:
            row = int(input(f"Player {current_player}, enter row (0-2): "))
            col = int(input(f"Player {current_player}, enter column (0-2): "))
        except ValueError:
            print("Please enter valid numbers (0, 1, or 2).")
            continue

        if row not in range(3) or col not in range(3):
            print("Invalid input. Please enter numbers between 0 and 2.")
            continue

        if board[row][col] != " ":
            print("Cell already taken. Try again.")
            continue

        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins! 🎉")
            break

        if is_full(board):
            print_board(board)
            print("It's a draw! 🤝")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"

def main():
    while True:
        play_game()
        again = input("Do you want to play again? (y/n): ").strip().lower()
        if again != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
