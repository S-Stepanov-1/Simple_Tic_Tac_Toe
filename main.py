# winner's verification and "Draw"
def wins(i, cell):
    win_list = [i, i, i]
    combinations = [cell[0:3], cell[3:6], cell[6::], cell[0:7:3],
                    cell[1:8:3], cell[2::3], cell[0::4], cell[2:7:2]]

    if win_list in combinations:
        matrix(grid)
        print(f"{i} wins")
        exit()
    elif " " not in grid:
        matrix(grid)
        print("Draw")
        exit()


# constructing an empty matrix
def matrix(xo):
    print('''---------''')
    print("|", xo[0], xo[1], xo[2], "|")
    print("|", xo[3], xo[4], xo[5], "|")
    print("|", xo[6], xo[7], xo[8], "|")
    print('''---------''')


# coordinate transformation into a matrix index
def coordinate_enter():
    i, j = input().split()  # enter of 2 numbers, coordinates
    check_numbers(i, j)


# only digits from 1 to 3 should be entered, check
def check_numbers(x, y):
    if x in "1234567890" and y in "1234567890":
        if x in "123" and y in "123":
            replace(int(x), int(y))
        else:
            print("Coordinates should be from 1 to 3!")
            coordinate_enter()
    else:
        print("You should enter numbers!")
        coordinate_enter()


# check the cell occupancy and update the matrix if everything is ok
def replace(c_1, c_2):
    index = ((c_1 - 1) * 3) + c_2 + 2 - 3  # index from 2 coordinates
    if grid[index] == "X" or grid[index] == "O":
        print("This cell is occupied! Choose another one!")
        coordinate_enter()
    elif counter % 2 != 0:
        grid[index] = "X"
        wins("X", grid)
    else:
        grid[index] = "O"
        wins("O", grid)


counter = 1
grid = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
while True:
    matrix(grid)  # constructing an empty matrix
    coordinate_enter()
    counter += 1
