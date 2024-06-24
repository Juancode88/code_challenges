"""
Write a program that it seems to tic-tac-toe
game with the equal function for the user and 
computer
"""
#Get the computer 
def computer_move(board):
    #Check if computer for the next mode 
    for i in range(3):
        for k in range (3):
            if board [i][k] == " ":
                board[i][k] = "O"
                if check_over(board) == "O":
                    return
                board[i][k] = " "
    #Check if the player can win in the next move 
    for i in range(3):
        for k in range(3):
            if board[i][k] == " ":
                board[i][k] = "X"
                if check_over(board) == "X":
                    board[i][k] = "O"
                    return
                board[i][k] = " "

    #random choice:
    for i in range(3):
        for k in range(3):
            if board[i][k] == " ":
                board [i][k] = "O"
            return 
def check_over(board):
    # Check rows and columns for a win
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]

    # Check diagonals for a win
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    # Check for a tie
    if all(cell != " " for row in board for cell in row):
        return "Tie"

    # Game is not over yet
    return None

def print_board(board):
    print(" " + board[0][0] + " | " + board[0][1] + " | " + board[0][2])
    print("---+---+---")
    print(" " + board[1][0] + " | " + board[1][1] + " | " + board[1][2])
    print("---+---+---")
    print(" " + board[2][0] + " | " + board[2][1] + " | " + board[2][2])

board = [[" "for _ in range(3)] for _ in range(3)]
while True:
    print_board(board)
    x,y = map(int, input("Enter your move (x y):").split())
    if board[x][y] != " ":
        print("Invalid move!")
        continue
    board[x][y] = "X"
    if check_over(board) == "X":
        print("You won!")
        break
    elif check_over(board) == "Tie":
        print("It's a tie!")
        break
    if computer_move(board) == "O":
        print("Computer Won!")
        break


