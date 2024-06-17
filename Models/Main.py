import time
from Board import Board
from ScoreBoard import ScoreBoard
from Game import Game

nickname = input("Enter your nickname: ")
scoreBoard = ScoreBoard()
game = Game("saperSavedGame")
print("New game - 1\n"
      "Load game - 2")
decision = int(input("Enter your decision: "))
wrong_number = True
while wrong_number:
    if decision == 1:
        board_x = int(input("Enter board size x. (Board size must be at least 5x5.): "))
        board_y = int(input("Enter board size y. (Board size must be at least 5x5.): "))
        board = Board(board_x, board_y)
        board.create_board()
        max_number_of_bombs = board_x * board_y // 2
        number_of_bombs = int(input("Enter number of bombs (Maximum number of bombs is " + str(max_number_of_bombs) + " Minimum number of bombs is 1.): "))
        board.insert_bombs(number_of_bombs)
        wrong_number = False
    elif decision == 2:
        board = Board(10, 10)
        game.load_game(board)
        wrong_number = False
    else:
        print("Invalid choice.")
        print("New game - 1\n"
              "Load game - 2")
        decision = int(input("Enter your decision: "))
board.print_board()
print("XXXXXXXXXXXXXXXXXXXXXXXX")
start_time = time.time()
while (True):
    print("check point - 1\n"
          "mark point with a flag - 2\n"
          "mark point with a question mark - 3\n"
          "save game - 4")
    decision2 = int(input(""))
    wrong_number = True
    while wrong_number:
        if decision2 == 1:
            x = int(input("Enter x: "))
            y = int(input("Enter y: "))
            v = board.check_point(x, y)
            if v == False:
                break
            board.print_board()
            wrong_number = False
        elif decision2 == 2:
            x = int(input("Enter x: "))
            y = int(input("Enter y: "))
            board.flag_point(x, y)
            board.print_board()
            wrong_number = False
        elif decision2 == 3:
            x = int(input("Enter x: "))
            y = int(input("Enter y: "))
            board.question_mark_point(x, y)
            board.print_board()
            wrong_number = False
        elif decision2 == 4:
            game.save_game(board)
            wrong_number = False
        else:
            print("Invalid choice.")
            print("check ponit - 1\n"
                  "mark point with a flag - 2\n"
                  "mark point with a question mark - 3\n"
                  "save game - 4")
            decision2 = int(input(""))

    print("XXXXXXXXXXXXXXXXXXXXXX")

