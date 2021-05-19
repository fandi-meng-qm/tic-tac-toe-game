# overall
best_place = (4, 0, 2, 6, 8, 1, 3, 5, 7)
win = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
X = "X"
O = "O"
EMPTY = "-"

# create board
def new_board():
    board = []
    for square in range(9):
        board.append(EMPTY)
    return board


# ask for the first player
def ask_yes_no(question):
    response = None
    while response not in ("y", "n"):
        response = input(question)
    return response

# beginner is X
def Pieces():
    go_first = ask_yes_no("Player first? (y/n): ")
    if go_first == "y":
        print("Player first.")
        human = X
        computer = O
    else:
        print("Computer first.")
        computer = X
        human = O
    return computer, human


# display board
def display_board(board):
    board2 = board[:]
    for i in range(9):
        if board[i] == EMPTY:
            board2[i] = i+1
    print("\t", board2[0], "|", board2[1], "|", board2[2])
    print("\t", "---------")
    print("\t", board2[3], "|", board2[4], "|", board2[5])
    print("\t", "---------")
    print("\t", board2[6], "|", board2[7], "|", board2[8], "\n")

def ask_number(question, low, high):
    response = None
    while response not in range(low, high):
        response = int(input(question))-1

    return response

#restriction
def legal_moves(board):
    moves = []
    for i in range(9):
        if board[i] == EMPTY:
            moves.append(i)
    return moves

def human_move(board, human):
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("player's choice? (1 - 9):", 0, 9)
        if move not in legal:
            print("\nWrong！")
    return move


def computer_move(board, computer, human):
    # make a copy to work with since function will be changing list
    board = board[:]
    # follow the best_place
    # if won，choose it
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print("Computer's choice is", move+1)
            return move
        # cancel
        board[move] = EMPTY
    # prevent player win
    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            print("Computer's choice is", move+1)
            return move
        # cancel
        board[move] = EMPTY

    # next place in list
    for move in best_place:
        if move in legal_moves(board):
            print("Computer's choice is", move+1)
            return move

# win or lose
def winner(board):
    for row in win:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
    # no place
    if EMPTY not in board:
        return "True"
    return False

# by turn
def next_turn(turn):
    if turn == X:
        return O
    else:
        return X


# main function
def main():
    computer, human = Pieces()
    turn = X
    board = new_board()
    display_board(board)
    the_winner = False
    while not the_winner:
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)
        the_winner = winner(board)
    # result
    if the_winner == computer:
        print("Computer win!\n")
    elif the_winner == human:
        print("Player win!\n")
    elif the_winner == "True":  # "平局"
        print("Draw.\n")


# start the program
main()
print("end")
