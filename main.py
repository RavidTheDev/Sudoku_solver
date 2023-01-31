import time
import pyautogui as pg

def is_valid_move(grid, row, col, number):

    for x in range(9):
        if grid[row][x] == number:
            return False

    for x in range(9):
        if grid[x][col] == number:
            return False

    corner_row = row - row % 3
    corner_col = col - col % 3

    for x in range(3):
        for y in range(3):
            if grid[corner_row + x][corner_col + y] == number:
                return False

    return True


def solve(grid, row, col):
    if col == 9:
        if row == 8:
            return True
        row += 1
        col = 0

    if grid[row][col] > 0:
        return solve(grid, row, col + 1)

    for num in range(1, 10):
        if is_valid_move(grid, row, col, num):
            grid[row][col] = num

            if solve(grid, row, col + 1):
                return True

        grid[row][col] = 0

    return False



grid = []
#
# [4, 0, 0, 0, 0, 5, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 1, 9, 8],
# [3, 0, 0, 0, 8, 2, 4, 0, 0],
# [0, 0, 0, 1, 0, 0, 0, 8, 0],
# [9, 0, 3, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 3, 0, 6, 7, 0],
# [0, 5, 0, 0, 0, 9, 0, 0, 0],
# [0, 0, 0, 2, 0, 0, 9, 0, 7],
# [6, 4, 0, 3, 0, 0, 0, 0, 0],
# ]


def print_and_solve(grid):
    if solve(grid,0,0):
        for i in range(9):
            for j in range(9):
                print(grid[i][j],end=" ")
            print()
    str_grid=[]

    for lists in grid:
        for n in lists:
            str_grid.append(str(n))


    counter=[]
    for number in str_grid:
        pg.press(number)
        pg.hotkey('right')
        counter.append(number)
        if len(counter)%9==0:
            pg.hotkey('down')
            for i in range(9):
                pg.hotkey('left')


    else:
        print("There is no solution for this sudoku !")

while True:

    row=list(input('Row: '))
    ints=[]
    for num in row:
        ints.append(int(num))
    grid.append(ints)

    if len(grid)==9:
        break
    print(f'Row {str(len(grid))} complete')

time.sleep(3)

print_and_solve(grid)