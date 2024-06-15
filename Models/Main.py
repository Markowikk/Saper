from Board import Board
import pprint

print("New game - 1\n"
      "Load game - 2")
dec = int(input("Enter your decision"))
b = Board(10, 10)
if dec == 1:
    b.create_board()
    x = int(input("Enter bombs"))
    b.insert_bombs(x)
elif dec == 2:
    b.load_game()
b.print_board()
print("XXXXXXXXXXXXXXXXXXXXXXXX")
while (True):
    print("check ponit - 1\n"
          "mark point with a flag - 2\n"
          "mark point with a mark - 3\n"
          "save game - 4")
    dec2 = int(input(""))
    if dec2 == 1:
        x = int(input("Enter x"))
        y = int(input("Enter y"))
        b.check_point(x, y)
        b.print_board()
    elif dec2 == 2:
        print("2")
    elif dec2 == 3:
        print("3")
    elif dec2 == 4:
        b.save_game()
    print("XXXXXXXXXXXXXXXXXXXXXX")
