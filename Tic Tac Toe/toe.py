import random

# Constants
EMPTY = ' '
PLAYER_X = 'X'
PLAYER_O = 'O'
BOARD_SIZE = 3

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * (BOARD_SIZE * 4 - 1))

def is_winner(board, player):
    for row in range(BOARD_SIZE):
        if all([cell == player for cell in board[row]]):
            return True
    for col in range(BOARD_SIZE):
        if all([board[row][col] == player for row in range(BOARD_SIZE)]):
            return True
    if all([board[i][i] == player for i in range(BOARD_SIZE)]):
        return True
    if all([board[i][BOARD_SIZE - 1 - i] == player for i in range(BOARD_SIZE)]):
        return True
    return False

def is_board_full(board):
    return all([cell != EMPTY for row in board for cell in row])

def get_available_moves(board):
    return [(r, c) for r in range(BOARD_SIZE) for c in range(BOARD_SIZE) if board[r][c] == EMPTY]

def evaluate(board):
    if is_winner(board, PLAYER_O):
        return 10
    elif is_winner(board, PLAYER_X):
        return -10
    return 0

def minimax(board, depth, is_maximizing):
    score = evaluate(board)

    if score == 10:
        return score
    if score == -10:
        return score
    if is_board_full(board):
        return 0

    if is_maximizing:
        best = -float('inf')
        for (r, c) in get_available_moves(board):
            board[r][c] = PLAYER_O
            best = max(best, minimax(board, depth + 1, not is_maximizing))
            board[r][c] = EMPTY
        return best
    else:
        best = float('inf')
        for (r, c) in get_available_moves(board):
            board[r][c] = PLAYER_X
            best = min(best, minimax(board, depth + 1, not is_maximizing))
            board[r][c] = EMPTY
        return best

def ai_move(board):
    best_val = -float('inf')
    best_move = None

    for (r, c) in get_available_moves(board):
        board[r][c] = PLAYER_O
        move_val = minimax(board, 0, False)
        board[r][c] = EMPTY

        if move_val > best_val:
            best_move = (r, c)
            best_val = move_val

    if best_move:
        board[best_move[0]][best_move[1]] = PLAYER_O

def player_move(board):
    while True:
        try:
            row = int(input("Enter the row (0, 1, or 2): "))
            col = int(input("Enter the column (0, 1, or 2): "))
            if (row, col) in get_available_moves(board):
                board[row][col] = PLAYER_X
                break
            else:
                print("Invalid move. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter numbers between 0 and 2.")

def main():
    board = [[EMPTY] * BOARD_SIZE for _ in range(BOARD_SIZE)]
    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        player_move(board)
        print_board(board)
        if is_winner(board, PLAYER_X):
            print("Congratulations! You win!")
            break
        if is_board_full(board):
            print("It's a tie!")
            break

        ai_move(board)
        print_board(board)
        if is_winner(board, PLAYER_O):
            print("AI wins! Better luck next time.")
            break
        if is_board_full(board):
            print("It's a tie!")
            break

if __name__ == "__main__":
    main()
