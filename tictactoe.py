import math

# Define constants for players
PLAYER_X = 'X'
PLAYER_O = 'O'
EMPTY = ' '

# Define the board size
BOARD_SIZE = 3

# Function to print the board
def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * (BOARD_SIZE * 2 - 1))

# Function to initialize a blank board
def initialize_board():
    return [[EMPTY for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

# Function to check if a player has won
def check_winner(board, player):
    # Check rows and columns
    for i in range(BOARD_SIZE):
        if all(board[i][j] == player for j in range(BOARD_SIZE)) or \
           all(board[j][i] == player for j in range(BOARD_SIZE)):
            return True
    
    # Check diagonals
    if all(board[i][i] == player for i in range(BOARD_SIZE)) or \
       all(board[i][BOARD_SIZE - i - 1] == player for i in range(BOARD_SIZE)):
        return True
    
    return False

# Function to check if the board is full
def is_board_full(board):
    return all(board[i][j] != EMPTY for i in range(BOARD_SIZE) for j in range(BOARD_SIZE))

# Function to get available moves
def get_available_moves(board):
    return [(i, j) for i in range(BOARD_SIZE) for j in range(BOARD_SIZE) if board[i][j] == EMPTY]

# Function to evaluate the board
def evaluate_board(board):
    if check_winner(board, PLAYER_X):
        return 1
    elif check_winner(board, PLAYER_O):
        return -1
    elif is_board_full(board):
        return 0
    else:
        return None

# Function to perform Minimax algorithm
def minimax(board, depth, is_maximizing):
    score = evaluate_board(board)

    if score is not None:
        return score

    if is_maximizing:
        best_score = -math.inf
        for i, j in get_available_moves(board):
            board[i][j] = PLAYER_X
            score = minimax(board, depth + 1, False)
            board[i][j] = EMPTY
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for i, j in get_available_moves(board):
            board[i][j] = PLAYER_O
            score = minimax(board, depth + 1, True)
            board[i][j] = EMPTY
            best_score = min(best_score, score)
        return best_score

# Function to find the best move using Minimax
def find_best_move(board):
    best_score = -math.inf
    best_move = None
    for i, j in get_available_moves(board):
        board[i][j] = PLAYER_X
        score = minimax(board, 0, False)
        board[i][j] = EMPTY
        if score > best_score:
            best_score = score
            best_move = (i, j)
    return best_move

# Function to play the game
def play_game():
    board = initialize_board()
    print_board(board)

    while True:
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter column (0-2): "))

        if board[row][col] != EMPTY:
            print("Invalid move. Please choose an empty spot.")
            continue

        board[row][col] = PLAYER_O
        print_board(board)

        if check_winner(board, PLAYER_O):
            print("You win!")
            break
        elif is_board_full(board):
            print("It's a tie!")
            break

        best_move = find_best_move(board)
        board[best_move[0]][best_move[1]] = PLAYER_X
        print("AI makes move at row {}, col {}".format(best_move[0], best_move[1]))
        print_board(board)

        if check_winner(board, PLAYER_X):
            print("AI wins!")
            break
        elif is_board_full(board):
            print("It's a tie!")
            break

# Start the game
play_game()
