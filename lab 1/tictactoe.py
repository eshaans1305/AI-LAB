import random

print("Eshaan S, 1BM24CS096")

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("---------")
2
def check_win(board, player):
    # Check rows
    for row in board:
        if all([cell == player for cell in row]):
            return True
    # Check columns
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    # Check diagonals
    if (board[0][0] == player and board[1][1] == player and board[2][2] == player) or \
       (board[0][2] == player and board[1][1] == player and board[2][0] == player):
        return True
    return False

def check_draw(board):
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True

def get_empty_cells(board):
    empty_cells = []
    for r in range(3):
        for c in range(3):
            if board[r][c] == ' ':
                empty_cells.append((r, c))
    return empty_cells

def minimax(board, depth, is_maximizing):
    if check_win(board, 'X'):
        return -10 + depth
    if check_win(board, 'O'):
        return 10 - depth
    if check_draw(board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for r, c in get_empty_cells(board):
            board[r][c] = 'O'
            score = minimax(board, depth + 1, False)
            board[r][c] = ' ' # Undo move
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for r, c in get_empty_cells(board):
            board[r][c] = 'X'
            score = minimax(board, depth + 1, True)
            board[r][c] = ' ' # Undo move
            best_score = min(score, best_score)
        return best_score

def ai_move(board):
    best_score = -float('inf')
    best_move = None
    for r, c in get_empty_cells(board):
        board[r][c] = 'O'
        score = minimax(board, 0, False)
        board[r][c] = ' ' # Undo move
        if score > best_score:
            best_score = score
            best_move = (r, c)
    return best_move

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X' # Player starts

    print("Welcome to Tic-Tac-Toe!\nYou are 'X', the AI is 'O'.")
    print_board(board)

    while True:
        if current_player == 'X':
            try:
                row = int(input("Enter row (0, 1, or 2): "))
                col = int(input("Enter column (0, 1, or 2): "))
                if not (0 <= row <= 2 and 0 <= col <= 2):
                    print("Invalid input. Row and column must be between 0 and 2.")
                    continue
                if board[row][col] != ' ':
                    print("Cell already taken. Try again.")
                    continue
                board[row][col] = 'X'
            except ValueError:
                print("Invalid input. Please enter numbers.")
                continue
        else:
            print("AI is making a move...")
            r, c = ai_move(board)
            board[r][c] = 'O'
        
        print_board(board)

        if check_win(board, current_player):
            print(f"{current_player} wins!")
            break
        elif check_draw(board):
            print("It's a draw!")
            break
        
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == '__main__':
    play_game()
