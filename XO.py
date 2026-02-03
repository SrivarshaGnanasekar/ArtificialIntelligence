PLAYER_A = 'X'
PLAYER_B = 'O'
EMPTY = ' '

def check_winner(board):
    # Check rows and columns for a winner
    for i in range(3):
        if all(board[i][j] == PLAYER_A for j in range(3)) or all(board[j][i] == PLAYER_A for j in range(3)):
            return PLAYER_A
        if all(board[i][j] == PLAYER_B for j in range(3)) or all(board[j][i] == PLAYER_B for j in range(3)):
            return PLAYER_B
    # Check diagonals for a winner
    if all(board[i][i] == PLAYER_A for i in range(3)) or all(board[i][2 - i] == PLAYER_A for i in range(3)):
        return PLAYER_A
    if all(board[i][i] == PLAYER_B for i in range(3)) or all(board[i][2 - i] == PLAYER_B for i in range(3)):
        return PLAYER_B
    return None

def is_full(board):
    return all(cell != EMPTY for row in board for cell in row)

def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == PLAYER_A:
        return 1
    elif winner == PLAYER_B:
        return -1
    elif is_full(board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_A
                    score = minimax(board, depth + 1, False)
                    board[i][j] = EMPTY
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_B
                    score = minimax(board, depth + 1, True)
                    board[i][j] = EMPTY
                    best_score = min(score, best_score)
        return best_score

def find_best_move(board):
    best_score = -float('inf')
    best_move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = PLAYER_A
                score = minimax(board, 0, False)
                board[i][j] = EMPTY
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    return best_move

def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('-' * 9)

def play_game():
    board = [[EMPTY for _ in range(3)] for _ in range(3)]
    current_player = PLAYER_A

    while True:
        print_board(board)
        if current_player == PLAYER_A:
            print("Player A's turn (X)")
            row, col = find_best_move(board)
        else:
            print("Player B's turn (O)")
            row, col = map(int, input("Enter row and column (0-2) separated by space: ").split())

        if board[row][col] != EMPTY:
            print("Invalid move! Try again.")
            continue

        board[row][col] = current_player
        winner = check_winner(board)

        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break
        elif is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = PLAYER_B if current_player == PLAYER_A else PLAYER_A

play_game()
