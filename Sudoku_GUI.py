from tkinter import *
from tkinter import messagebox
import Sudoku_BackTrack
import time
import copy

root = Tk()
root.title("Sudoku Solver")
root.geometry("600x600")
root.iconbitmap("C:/Я картинки/Милыйдинозавр.ico")

grid = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]]

grid1 = [[7, 8, 0, 4, 3, 0, 1, 2, 0],
         [6, 0, 0, 0, 7, 5, 0, 0, 9],
         [0, 0, 0, 6, 0, 1, 0, 7, 8],
         [0, 0, 7, 0, 4, 0, 2, 6, 0],
         [0, 0, 1, 0, 5, 0, 9, 3, 0],
         [9, 0, 4, 0, 6, 0, 0, 0, 5],
         [0, 7, 0, 3, 0, 0, 0, 1, 2],
         [1, 2, 0, 0, 0, 7, 4, 0, 0],
         [0, 4, 9, 2, 0, 6, 0, 0, 7]]  # last one should be 7 instead of 8

board = copy.deepcopy(grid1)
# board = [[0 for i in range(9)] for j in range(9)]

Entries = []

frame_side_length = 150  # 150x150
frame_background_color = '#303030'

cell_side_length = 49  # 50x50

# FRAME = Frame(root, bg=frame_background_color).place(x=0, y=0, width=455, height=455)

# Generating 81 entries
def fill_all(list):
    for row in range(9):
        list.insert(row, [])
        for col in range(9):
            list[row].append(Entry(root, bg='white', justify='center', font=('Helvetica', 14)))
            list[row][col].place(x=col * cell_side_length + 5,
                                 y=row * cell_side_length + 5,
                                 width=cell_side_length,
                                 height=cell_side_length)
    return list

Entries = fill_all(Entries)

# Delete all zeros in default grid
def delete_Zero():
    for r in range(9):
        for c in range(9):
            if Entries[r][c].get() == '0':
                Entries[r][c].delete(0, END)
            # else:
            #     Entries[r][c].config()  # I wanted to change view of unchangeable numbers
    return Entries


# Entering any values
def insert_values(grid):
    for row in range(9):
        for col in range(9):
            Entries[row][col].delete(0)  # that's why I need this function to delete unwanted values
            Entries[row][col].insert(0, grid[row][col])  # don't know why, it inserts all previous values
    delete_Zero()
    return Entries

# Setting default values
def set_default_values(grid):
    insert_values(grid)
    solve_btn.config(state=ACTIVE)


# function to clear board
def clear_board(board):
    for r in range(9):
        for c in range(9):
            Entries[r][c].delete(0, END)
    time_lbl.config(text='')
    solve_btn.config(state=DISABLED)
    return Entries


def is_number(num):
    try:
        int(num)
        return True
    except:
        return False


# Enter users values
def check_user_values():
    found = False
    for r in range(9):
        for c in range(9):
            if is_number(Entries[r][c].get()):
                if abs(int(Entries[r][c].get())) >= 10:
                    found = True
                    Entries[r][c].delete(0, END)
            elif Entries[r][c].get() != '':
                found = True
                Entries[r][c].delete(0, END)
    if found:
        messagebox.showerror('Ho Hey!', 'You can type only numbers < 10')


# Function to set new values
def set_values(board):
    solve_btn.config(state=DISABLED)
    clear_board(board)
    call_done_btn()


# call for done button again
def call_done_btn():
    global done_btn
    messagebox.showinfo("Ho hey!", 'Enter your numbers\nTap button "Done!" when you are done')
    done_btn = Button(root, text='Done!', command=lambda: Done(board))
    done_btn.place(x=475, y=400, width=50, height=30)


# done entering user values function
def Done(board):
    check_user_values()
    done_btn.destroy()
    solve_btn.config(state=ACTIVE)
    for row in range(9):
        for col in range(9):
            if is_number(Entries[row][col].get()):
                board[row][col] = int(Entries[row][col].get())
            else:
                board[row][col] = 0
    # Sudoku_BackTrack.print_sudoku(board)
    insert_values(board)
    return board


# solving function
def solve(puzzle):
    global time_lbl
    start = time.time()
    puzzle_copy = copy.deepcopy(puzzle)
    if not Sudoku_BackTrack.solve(puzzle_copy):
        messagebox.showwarning('Ho hey!', 'Sudoku can not be solved')
    insert_values(puzzle_copy)
    end = round(time.time() - start, 2)
    time_lbl = Label(root, text=str(end) + ' sec')
    time_lbl.place(x=400, y=475, width=150, height=30)


# Creating buttons and drops
# Solve button
solve_btn = Button(root, text='Solve!', command=lambda: solve(board))
solve_btn.place(x=475, y=125, width=100, height=50)

# Set your values again button
set_again_btn = Button(root, text='Set', command=lambda: set_values(board))
set_again_btn.place(x=475, y=200, width=50, height=50)

# Default? button
default_btn = Button(root, text='Default?', command=lambda: set_default_values(board))
default_btn.place(x=10, y=475, width=100, height=50)

# Clear button
clear_btn = Button(root, text='Clear', command=lambda: clear_board(board))
clear_btn.place(x=120, y=475, width=100, height=50)


# Time label showing time
time_lbl = Label(root)

# Drop to choose algorithm
options = ('BackTrack',
           'AI',
           'Algorithm')

choosed = StringVar()
choosed.set(options[0])

Label(root, text='Choose\nsolving\nalgorithm').place(x=475, y=10, width=100, height=50)
drop = OptionMenu(root, choosed, *options)
drop.place(x=475, y=75, width=100, height=40)

# Creating messageBox to set default or users values
response = messagebox.askyesno("Ho hey!", "Do you want to set default values?") # equals 1 or 0
if response:
    insert_values(board)
else:
    solve_btn.config(state=DISABLED)
    call_done_btn()

mainloop()

'''|  With Frames (not working well)
   v'''
# # First try to make GUI with tkinter
# from tkinter import *
# from tkinter import messagebox
# import Sudoku_BackTrack
# import time
# import copy
#
# root = Tk()
# root.title("Sudoku Solver")
# root.geometry("600x600")
# root.iconbitmap("C:/Я картинки/Милыйдинозавр.ico")
#
# grid = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
#         [6, 0, 0, 1, 9, 5, 0, 0, 0],
#         [0, 9, 8, 0, 0, 0, 0, 6, 0],
#         [8, 0, 0, 0, 6, 0, 0, 0, 3],
#         [4, 0, 0, 8, 0, 3, 0, 0, 1],
#         [7, 0, 0, 0, 2, 0, 0, 0, 6],
#         [0, 6, 0, 0, 0, 0, 2, 8, 0],
#         [0, 0, 0, 4, 1, 9, 0, 0, 5],
#         [0, 0, 0, 0, 8, 0, 0, 7, 9]]
#
# grid1 = [[7, 8, 0, 4, 3, 0, 1, 2, 0],
#          [6, 0, 0, 0, 7, 5, 0, 0, 9],
#          [0, 0, 0, 6, 0, 1, 0, 7, 8],
#          [0, 0, 7, 0, 4, 0, 2, 6, 0],
#          [0, 0, 1, 0, 5, 0, 9, 3, 0],
#          [9, 0, 4, 0, 6, 0, 0, 0, 5],
#          [0, 7, 0, 3, 0, 0, 0, 1, 2],
#          [1, 2, 0, 0, 0, 7, 4, 0, 0],
#          [0, 4, 9, 2, 0, 6, 0, 0, 8]]  # last one should be 7 instead of 8
#
# board = copy.deepcopy(grid)
# # board = [[0 for i in range(9)] for j in range(9)]
#
# Frames = []
# Entries = []
#
# frame_side_length = 150  # 150x150
# frame_background_color = '#303030'
#
# cell_side_length = 49  # 50x50
#
#
# # Generating 9 frames
# def frames_and_entries(frame_list):
#     for row in range(3):
#         for col in range(3):
#             frame_list.append((
#                 Frame(root, bg=frame_background_color).place(x=col * frame_side_length, y=row * frame_side_length,
#                                                              width=frame_side_length,
#                                                              height=frame_side_length), (row * 3, col * 3)))
#     return frame_list
#
#
# Frames_and_positions = frames_and_entries(Frames)
#
# '''
#  shift:             0        frame_side   2*frame_side
# 0                   []           []              []
#
# frame_side          []           []              []
#
# 2*frame_side        []           []              []
# '''
# Shifts = [(0, 0), (frame_side_length, 0), (2 * frame_side_length, 0),
#           (0, frame_side_length), (frame_side_length, frame_side_length), (2 * frame_side_length, frame_side_length),
#           (0, 2 * frame_side_length), (frame_side_length, 2 * frame_side_length),
#           (2 * frame_side_length, 2 * frame_side_length)]
#
#
# # Generating 81 entries
# def fill_all(frames, entries):
#     for k in range(len(frames)):
#         list = []
#         x_shift, y_shift = Shifts[k][0], Shifts[k][1]
#         for row in range(3):
#             list.insert(row, [])
#             for col in range(3):
#                 list[row].append(Entry(frames[k][0], bg='white', justify='center', font=('Helvetica', 14)))
#                 list[row][col].place(x=x_shift + col * cell_side_length + 1,
#                                      y=y_shift + row * cell_side_length + 1,
#                                      width=cell_side_length,
#                                      height=cell_side_length)
#         entries.append(list)
#     return entries
#
#
# Entries = fill_all(Frames_and_positions, Entries)
#
#
# # Delete all zeros in default grid
# def delete_Zero():
#     for k in range(len(Frames)):
#         for r in range(3):
#             for c in range(3):
#                 if Entries[k][r][c].get() == '0':
#                     Entries[k][r][c].delete(0, END)
#                 # else:
#                 #     Entries[k][r][c].config()  # I wanted to change view of unchangeable numbers
#     return Entries
#
#
# # Entering any values
# def insert_values(grid):
#     for k in range(len(Frames)):
#         for row in range(Frames[k][1][0] + 3):  # rows_start == Frames[k][1][0]
#             for col in range(Frames[k][1][1] + 3):  # columns_start == Frames[k][1][1]
#                 Entries[k][row % 3][col % 3].delete(0)  # that's why I need this function to delete unwanted values
#                 Entries[k][row % 3][col % 3].insert(0, grid[row][col])  # don't know why, it inserts all previous values
#     delete_Zero()
#     return Entries
#
#
# # function to clear board
# def clear_board():
#     for k in range(len(Frames)):
#         for r in range(3):
#             for c in range(3):
#                 Entries[k][r][c].delete(0, END)
#     time_lbl.config(text='')
#     return Entries
#
#
# def is_number(num):
#     try:
#         int(num)
#         return True
#     except:
#         return False
#
#
# # Enter users values
# def check_user_values():
#     found = False
#     for k in range(len(Frames)):
#         for r in range(3):
#             for c in range(3):
#                 if is_number(Entries[k][r][c].get()):
#                     if abs(int(Entries[k][r][c].get())) >= 10:
#                         found = True
#                         Entries[k][r][c].delete(0, END)
#                 elif Entries[k][r][c].get() != '':
#                     found = True
#                     Entries[k][r][c].delete(0, END)
#     if found:
#         messagebox.showerror('Ho Hey!', 'You can type only numbers < 10')
#
#
# # done entering user values function
# def Done(board):
#     check_user_values()
#     done_btn.destroy()
#     for k in range(len(Frames)):
#         for row in range(Frames[k][1][0] + 3):
#             for col in range(Frames[k][1][1] + 3):
#                 # print(is_number(Entries[k][row % 3][col % 3].get()), end=' ')
#                 if is_number(Entries[k][row % 3][col % 3].get()):
#                     board[row][col] = int(Entries[k][row % 3][col % 3].get())
#                     # Entries[k][row % 3][col % 3].delete(0, END)
#                 # if Entries[k][row % 3][col % 3].get() == '':
#                 #     board[row][col] = 0
#                 # Entries[k][row % 3][col % 3].delete(0, END)
#             # print(k, '\n')
#     Sudoku_BackTrack.print_sudoku(board)
#     insert_values(board)
#     return board
#
#
# # solving function
# def solve(puzzle):
#     global time_lbl
#     start = time.time()
#     puzzle_copy = copy.deepcopy(puzzle)
#     if not Sudoku_BackTrack.solve(puzzle_copy):
#         messagebox.showwarning('Ho hey!', 'Sudoku can not be solved')
#     insert_values(puzzle_copy)
#     end = time.time() - start
#     time_lbl = Label(root, text=str(end) + ' sec')
#     time_lbl.place(x=400, y=475, width=150, height=30)
#
#
# # Creating buttons and drops
# # Solve button
# solve_btn = Button(root, text='Solve!', command=lambda: solve(board))
# solve_btn.place(x=475, y=125, width=100, height=50)
#
# # Time label showing time
# time_lbl = Label(root)
#
# # Default? button
# default_btn = Button(root, text='Default?', command=lambda: insert_values(board))
# default_btn.place(x=10, y=475, width=100, height=50)
#
# # Clear button
# clear_btn = Button(root, text='Clear', command=clear_board)
# clear_btn.place(x=120, y=475, width=100, height=50)
#
# # Drop to choose algorithm
# options = ('BackTrack',
#            'AI',
#            'Algorithm')
#
# choosed = StringVar()
# choosed.set(options[0])
#
# Label(root, text='Choose\nsolving\nalgorithm').place(x=475, y=10, width=100, height=50)
# drop = OptionMenu(root, choosed, *options)
# drop.place(x=475, y=75, width=100, height=40)
#
# # Creating messageBox to set default or users values
# response = messagebox.askyesno("Ho hey!", "Do you want to set default values?")
# if response == 1:
#     insert_values(grid)
# else:
#     messagebox.showinfo("Ho hey!", 'Enter your numbers\nTap button "Done!" when your done')
#     done_btn = Button(root, text='Done!', command=lambda: Done(board))
#     done_btn.place(x=475, y=400, width=50, height=30)
#
# mainloop()
