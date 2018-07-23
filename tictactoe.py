
#print("\033[1;32;38m green")
#print("\033[1;31;38m red")
#print("\033[1;30;38m white")


map = ["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]

x_win = False
o_win = False
draw = 0
while not x_win and not o_win and draw < 9:
    if map[0][0] == "X" and map[0][1] == "X" and map[0][2] =="X" or map[1][0] == "X" and map[1][1] == "X" and map[1][2] =="X" or map[2][0] == "X" and map[2][1] == "X" and map[2][2] =="X" or map[0][0] == "X" and map[1][0] == "X" and map[2][0] =="X" or map[0][1] == "X" and map[1][1] == "X" and map[2][1] =="X" or map[0][2] == "X" and map[1][2] == "X" and map[2][2] =="X" or map[0][0] == "X" and map[1][1] == "X" and map[2][2] =="X" or map[2][0] == "X" and map[1][1] == "X" and map[0][2] =="X":
        x_win = True
    elif map[0][0] == "O" and map[0][1] == "O" and map[0][2] =="O" or map[1][0] == "O" and map[1][1] == "O" and map[1][2] =="O" or map[2][0] == "O" and map[2][1] == "O" and map[2][2] =="O" or map[0][0] == "O" and map[1][0] == "O" and map[2][0] =="O" or map[0][1] == "O" and map[1][1] == "O" and map[2][1] =="O" or map[0][2] == "O" and map[1][2] == "O" and map[2][2] =="O" or map[0][0] == "O" and map[1][1] == "O" and map[2][2] =="O" or map[2][0] == "O" and map[1][1] == "O" and map[0][2] =="O":
        o_win = True
    else:
        x_turn = True
    while x_turn and draw < 9:
        print("\n" + map[0][0] + " | " + map[0][1] + " | " + map[0][2])
        print("---------")
        print(map[1][0] + " | " + map[1][1] + " | " + map[1][2])
        print("---------")
        print(map[2][0] + " | " + map[2][1] + " | " + map[2][2] + "\n")
        choice = input("Place X: ")
        if choice == "1" and map[0][0] != "X" and map[0][0] != "O":
            map[0][0] = "X"
            x_turn = False
            draw += 1
        elif choice == "2" and map[0][1] != "X" and map[0][1] != "O":
            map[0][1] = "X"
            x_turn = False
            draw += 1
        elif choice == "3" and map[0][2] != "X" and map[0][2] != "O":
            map[0][2] = "X"
            x_turn = False
            draw += 1
        elif choice == "4" and map[1][0] != "X" and map[1][0] != "O":
            map[1][0] = "X"
            x_turn = False
            draw += 1
        elif choice == "5" and map[1][1] != "X" and map[1][1] != "O":
            map[1][1] = "X"
            x_turn = False
            draw += 1
        elif choice == "6" and map[1][2] != "X" and map[1][2] != "O":
            map[1][2] = "X"
            x_turn = False
            draw += 1
        elif choice == "7" and map[2][0] != "X" and map[2][0] != "O":
            map[2][0] = "X"
            x_turn = False
            draw += 1
        elif choice == "8" and map[2][1] != "X" and map[2][1] != "O":
            map[2][1] = "X"
            x_turn = False
            draw += 1
        elif choice == "9" and map[2][2] != "X" and map[2][2] != "O":
            map[2][2] = "X"
            x_turn = False
            draw += 1
        else:
            print("Invalid input, try again.")
        if map[0][0] == "X" and map[0][1] == "X" and map[0][2] == "X" or map[1][0] == "X" and map[1][1] == "X" and \
                map[1][2] == "X" or map[2][0] == "X" and map[2][1] == "X" and map[2][2] == "X" or map[0][0] == "X" and \
                map[1][0] == "X" and map[2][0] == "X" or map[0][1] == "X" and map[1][1] == "X" and map[2][1] == "X" or \
                map[0][2] == "X" and map[1][2] == "X" and map[2][2] == "X" or map[0][0] == "X" and map[1][1] == "X" and \
                map[2][2] == "X" or map[2][0] == "X" and map[1][1] == "X" and map[0][2] == "X":
            x_win = True
        elif map[0][0] == "O" and map[0][1] == "O" and map[0][2] == "O" or map[1][0] == "O" and map[1][1] == "O" and \
                map[1][2] == "O" or map[2][0] == "O" and map[2][1] == "O" and map[2][2] == "O" or map[0][0] == "O" and \
                map[1][0] == "O" and map[2][0] == "O" or map[0][1] == "O" and map[1][1] == "O" and map[2][1] == "O" or \
                map[0][2] == "O" and map[1][2] == "O" and map[2][2] == "O" or map[0][0] == "O" and map[1][1] == "O" and \
                map[2][2] == "O" or map[2][0] == "O" and map[1][1] == "O" and map[0][2] == "O":
            o_win = True
        else:
            o_turn = True
    while not x_turn and o_turn and draw < 9:
        print("\n" + map[0][0] + " | " + map[0][1] + " | " + map[0][2])
        print("---------")
        print(map[1][0] + " | " + map[1][1] + " | " + map[1][2])
        print("---------")
        print(map[2][0] + " | " + map[2][1] + " | " + map[2][2] + "\n")
        choice = input("Place O: ")
        if choice == "1" and map[0][0] != "X" and map[0][0] != "O":
            map[0][0] = "O"
            o_turn = False
            draw += 1
        elif choice == "2" and map[0][1] != "X" and map[0][1] != "O":
            map[0][1] = "O"
            o_turn = False
            draw += 1
        elif choice == "3" and map[0][2] != "X" and map[0][2] != "O":
            map[0][2] = "O"
            o_turn = False
            draw += 1
        elif choice == "4" and map[1][0] != "X" and map[1][0] != "O":
            map[1][0] = "O"
            o_turn = False
            draw += 1
        elif choice == "5" and map[1][1] != "X" and map[1][1] != "O":
            map[1][1] = "O"
            o_turn = False
            draw += 1
        elif choice == "6" and map[1][2] != "X" and map[1][2] != "O":
            map[1][2] = "O"
            o_turn = False
            draw += 1
        elif choice == "7" and map[2][0] != "X" and map[2][0] != "O":
            map[2][0] = "O"
            o_turn = False
            draw += 1
        elif choice == "8" and map[2][1] != "X" and map[2][1] != "O":
            map[2][1] = "O"
            o_turn = False
            draw += 1
        elif choice == "9" and map[2][2] != "X" and map[2][2] != "O":
            map[2][2] = "O"
            o_turn = False
            draw += 1
        else:
            print("Invalid input, try again.")

if x_win:
    print("X is the winner!")
elif o_win:
    print("O is the winner!")
else:
    print("Draw")

input("Press Enter to exit.")