import numpy as np


def input_grid(grid):
	# Validated Input Int
	if grid.isdigit() and int(grid) <= 50 and int(grid) > 0:
		pass
	else:
		return False

	grid_down = int(grid) + 1

	if len(str(grid)) > 1:
		grids_up = '{}'.format(grid)
		grids_down = '{}'.format(grid_down)
	else:
		grids_up = '0{}'.format(grid)
		grids_down = '{}'.format(grid_down) if len(str(grid_down)) > 1 else '0{}'.format(grid_down)


	# Open sudoku.txt file
	f = open("sudoku.txt", "r")
	up = f.read().split('Grid {}'.format(grids_up))[1]
	down = up.split('Grid {}'.format(grids_down))[0]

	l_su = []
	for d in down:
		split_data = []
		if '\n' not in d:
			l_su.append(int(d))

	new_sudoku = np.array_split(np.array(l_su), 9)
	board = []
	for nw in new_sudoku:
		board.append(nw.tolist())

	return board


def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False


def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col

    return None


def calculated(bo):
	incr_list = bo[0][0:3]
	incr = int(0)
	for i in incr_list:
		incr = incr + i
	print("%s = %s" % (" + ".join(str(i) for i in incr_list) , incr), '\n')


grid = input("There Are 1-50 grids \nPlease Input Grid To Be Solved : ")
board = input_grid(grid)

if board == False:
	print("Please, Input as digit Number (1 - 50).!")
else:
	print("\n")
	print_board(board)
	solve(board)

	print("\n", "_________+__________", "\n")

	print_board(board)

	print("\n", "_________+__________", "\n")

	calculated(board)
