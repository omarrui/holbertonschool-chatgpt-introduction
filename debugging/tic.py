#!/usr/bin/python3
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " " or \
           board[0][i] == board[1][i] == board[2][i] != " ":
            return True
    
    if board[0][0] == board[1][1] == board[2][2] != " " or \
       board[0][2] == board[1][1] == board[2][0] != " ":
        return True
    
    return False

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    current_player = "X"
    
    while True:
        print_board(board)
        
        while True:
            try:
                row = int(input(f"Enter row (0, 1, or 2) for player {current_player}: "))
                col = int(input(f"Enter column (0, 1, or 2) for player {current_player}: "))
                if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == " ":
                    break
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Please enter valid numbers.")
        
        board[row][col] = current_player
        
        if check_winner(board):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break
        
        current_player = "O" if current_player == "X" else "X"

tic_tac_toe()
