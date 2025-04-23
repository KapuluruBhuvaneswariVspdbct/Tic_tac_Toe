def print_board(board):
    print("\nCurrent board:")
    size = len(board)
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i != size - 1:
            print("-" * (4 * size - 3))
    print()

def check_winner(board, player, win_length):
    size = len(board)

    # Check rows and columns for win_length consecutive marks
    for i in range(size):
        for j in range(size - win_length + 1):
            # Check horizontal line
            if all(board[i][j+k] == player for k in range(win_length)):
                return True
            # Check vertical line
            if all(board[j+k][i] == player for k in range(win_length)):
                return True

    # Check diagonals (\\ and /)
    for i in range(size - win_length + 1):
        for j in range(size - win_length + 1):
            # Check main diagonal (\\)
            if all(board[i+k][j+k] == player for k in range(win_length)):
                return True
            # Check anti-diagonal (/)
            if all(board[i+k][j+win_length-1-k] == player for k in range(win_length)):
                return True
    return False

def is_draw(board):
    return all(cell in ['X', 'O'] for row in board for cell in row)

def get_move(max_num):
    while True:
        try:
            choice = int(input(f"Enter your move (1-{max_num}): "))
            if 1 <= choice <= max_num:
                return choice
            else:
                print(f"Choose a number between 1 and {max_num}.")
        except ValueError:
            print("Invalid input. Enter a number.")

def display_win_conditions(size, win_length):
    print(f"\n🎯 To win on a {size}x{size} board, you need {win_length} in a row.\n")
    print("Examples of winning lines:\n")

    # Horizontal
    print("Horizontal: ", end="")
    print(" | ".join(['X'] * win_length))

    # Vertical
    print("Vertical:")
    for _ in range(win_length):
        print("X")

    # Diagonal
    print("Diagonal (\\):")
    for i in range(win_length):
        print("    " * i + "X")

    # Anti-Diagonal
    print("Diagonal (/):")
    for i in range(win_length):
        print("    " * (win_length - i - 1) + "X")
    print()

def tic_tac_toe():
    while True:
        try:
            size = int(input("Enter board size (e.g. 3, 4, 5...): "))
            if size < 3:
                print("Minimum size is 3.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    # Decide win condition based on size
    win_length = size if size < 5 else 5
    display_win_conditions(size, win_length)

    board = [[str(i * size + j + 1) for j in range(size)] for i in range(size)]
    players = ['X', 'O']
    turn = 0
    total_moves = size * size

    while True:
        print_board(board)
        current_player = players[turn % 2]
        print(f"Player {current_player}'s turn.")

        move = get_move(total_moves)
        row, col = (move - 1) // size, (move - 1) % size

        if board[row][col] in ['X', 'O']:
            print("That position is already taken. Try again.")
            continue

        board[row][col] = current_player

        if check_winner(board, current_player, win_length):
            print_board(board)
            print(f"🎉 Player {current_player} wins!")
            break

        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        turn += 1

# Run the game
tic_tac_toe()
