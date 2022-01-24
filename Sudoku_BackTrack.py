import time


# Printing sudoku fuction
def print_sudoku(puzzle):
    # for i in range(0, 9):
    #     print(i, end=' ')
    # print('\n')
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            print(puzzle[i][j], end=' ')
        print()


# Find a free cell in sudoku function
def find_cell(sudoku):
    for i in range(len(sudoku)):
        for j in range(len(sudoku[i])):
            if sudoku[i][j] == 0:
                r, c = i, j
                return r, c
    return None, None


# Try all numbers from 1 to 9 in empty cell function
def try_all_numbers(sudoku, r, c, number):
    # If number in a row
    if number in sudoku[r]:
        return False
    # If number in a column
    for i in range(len(sudoku)):
        if number == sudoku[i][c]:
            return False
    # Find 3x3 square where the cell is
    r_start = r // 3 * 3
    c_start = c // 3 * 3
    # If number in a square
    for row in range(r_start, r_start + 3):
        for col in range(c_start, c_start + 3):
            if number == sudoku[row][col]:
                return False
    return True


# Solving function
def solve(sudoku):
    r, c = find_cell(sudoku)
    if r is None:
        return True
    for number in range(1, 10):
        if try_all_numbers(sudoku, r, c, number):
            sudoku[r][c] = number

            if solve(sudoku):
                return True

        sudoku[r][c] = 0


puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
          [6, 0, 0, 1, 9, 5, 0, 0, 0],
          [0, 9, 8, 0, 0, 0, 0, 6, 0],
          [8, 0, 0, 0, 6, 0, 0, 0, 3],
          [4, 0, 0, 8, 0, 3, 0, 0, 1],
          [7, 0, 0, 0, 2, 0, 0, 0, 6],
          [0, 6, 0, 0, 0, 0, 2, 8, 0],
          [0, 0, 0, 4, 1, 9, 0, 0, 5],
          [0, 0, 0, 0, 8, 0, 0, 7, 9]]

puzzle_real_from_app = [[9, 8, 4, 0, 0, 0, 5, 0, 1],
                        [0, 0, 0, 5, 0, 0, 0, 0, 7],
                        [0, 0, 0, 0, 0, 0, 0, 0, 9],
                        [0, 0, 0, 0, 1, 0, 0, 0, 0],
                        [0, 2, 0, 7, 0, 3, 1, 0, 0],
                        [5, 6, 0, 0, 0, 0, 0, 0, 0],
                        [8, 0, 0, 0, 0, 0, 4, 9, 6],
                        [0, 0, 0, 0, 9, 0, 0, 0, 0],
                        [1, 0, 0, 2, 8, 0, 0, 0, 0]]

'''
puzzle_unreal = [[0 for i in range(9)] for j in range(9)]
puzzle_unreal[1][0] = 1
puzzle_unreal[0][1] = 2
puzzle_unreal[2][0] = 3

start = time.time()
print_sudoku(puzzle_unreal)
print('\n')
solve(puzzle_unreal)
print_sudoku(puzzle_unreal)

print("\nTime is", time.time() - start, 'seconds')
'''
# sudoku(puzzle)
# # Should return
#  [[5,3,4,6,7,8,9,1,2],
#   [6,7,2,1,9,5,3,4,8],
#   [1,9,8,3,4,2,5,6,7],
#   [8,5,9,7,6,1,4,2,3],
#   [4,2,6,8,5,3,7,9,1],
#   [7,1,3,9,2,4,8,5,6],
#   [9,6,1,5,3,7,2,8,4],
#   [2,8,7,4,1,9,6,3,5],
#   [3,4,5,2,8,6,1,7,9]]
