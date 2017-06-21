import random


def display_board(board):
    row = 0
    column = 0
    print("  | 1 2 3 ")
    print("--+-------")
    for row in range(1, 3):
        print(row, " | ")
        for column in range(1, 3):
            print(board[column][row], " ", endl="/n")
        print(" ")

        
def clear_board():
    board = [["" for i in range(1, 3)] for j in range(1, 3)]
    row = 0
    column = 0
    for row in range(1, 3):
        for column in range(1, 3):
            board[column][row] = ""
    return board

            
def get_move_coordinates():
    x_coord = input("Enter x coordinate: ")
    y_coord = input("Enter y coordinate: ")
    print(" ")
    return x_coord, y_coord


def check_valid_move(x_coord, y_coord, board):
    valid_move = True
    
    # Check x coordinate is vaild
    if x_coord < 1 or x_coord > 3:
        valid_move = False
        
    return valid_move


def check_x_or_o_has_won(board):
    row = 0
    column = 0
    x_or_o_has_won = False

    for column in range(1, 3):
        if board[column][1] == board[column][2] and board[column][2] == board[column][3] and board[column][2] != "":
            x_or_o_has_won = True
    for row in range(1, 3):
        if board[1][row] == board[2][row] and board[2][row] == board[3][row] and board[2][row] != "":
            x_or_o_has_won = True
            
    return x_or_o_has_won


def get_who_starts():
    rand_num = random.randint(0, 100)
    who_starts = ""
    if rand_num % 2 == 0:
        who_starts = "X"
    else:
        who_starts = "O"
    return who_starts


if __name__ == "__main__":
    p1name = input("What is the name of player one?")
    p2name = input("What is the name of player two?")
    print(" ")
    p1score = 0
    p2score = 0
    p1symbol = ""
    p2symbol = ""

    # Choosing a player's symbol
    while True:
        p1symbol = (input(p1name + " what symbol do you wish to use, X or O?")).upper()
        print(" ")
        if p1symbol not in ["X" or "O"]:
            print("Entered symbol must be X or O", endl="/n")
        else:
            break
        
    if p1symbol == "X":
        p2symbol == "O"
    else:
        p2symbol == "X"
        
    start_symbol = get_who_starts()


    # The game starts here
    while True:
        num_moves = 0
        game_drawn = False
        game_won = False
        board = clear_board()
        print(" ")
        display_board(board)

        if start_symbol == p1symbol:
            print(p1name, " starts playing ", start_symbol)
        else:
            print(p2name, " starts playing ", start_symbol)
        print(" ")

        current_symbol = start_symbol

        # Play until a player wins or the game is drawn
        while True:
            # Get a valid move
            while True:
                x_coord, y_coord = get_move_coordinates()
                valid_move = check_valid_move(x_coord, y_coord, board)
                if not valid_move:
                    print("Coordinates invalid, please try again")
                else:
                    break
            board[x_coord][y_coord] = current_symbol
            display_board(board)
            game_won = check_x_or_o_has_won(board)
            num_moves += 1
            if not game_won:
                # Check if maximum number of allowed moves has been reached
                if num_moves == 9:
                    game_drawn = True
                else:
                    if current_symbol == "X":
                        current_symbol == "O"
                    else:
                        current_symbol == "X"
            if game_won or game_drawn:
                break

            # Update scores and display result
            if game_won:
                if p1symbol == current_symbol:
                    print(p1name, " congratulations you win!")
                    p1score += 1
                else:
                    print(p2name, " congratulations you win!")
                    p2score += 1
            else:
                print("A draw this time!")
            print(" ")
            print(p1name, " your score is: ", p1score)
            print(p2name, " your score is: ", p2score)
            print(" ")

            if start_symbol == p1symbol:
                start_symbol == p2symbol
            else:
                start_symbol == p1symbol
                
            while True:
                answer = input("Another game? (Y/N)").lower()
                if answer != "y" or answer != "n":
                    print("Please answer Y or N")
            if answer == "n":
                break
