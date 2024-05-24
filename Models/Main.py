from Board import Board
import pprint

b = Board(3, 3)
b.create_board()
b.print_board()
print("XXXXXXXXXXXXXXXXXXXXXXXX")
x = int(input("Enter bombs"))
b.insert_bombs(x)
b.test()
b.print_board()
# while (True):
#     x = int(input("Enter x"))
#     y = int(input("Enter y"))
#     b.check_point(x, y)
#     b.print_board()
#     print("XXXXXXXXXXXXXXXXXXXXXX")
