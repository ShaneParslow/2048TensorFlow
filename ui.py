import tkinter as tk

def init_ui(size):
    global window
    global ui_board
    window = tk.Tk()

    # Fill UI board with zeroes
    ui_board = [[tk.Label(window,text="0") for i in range(size)] for j in range(size)]
    # Setup geometry managers for each label in ui_board
    row_iterator = 0
    for row in ui_board:
        label_iterator = 0
        for label in row:
            ui_board[row_iterator][label_iterator].grid(row=row_iterator,column=label_iterator)
            label_iterator += 1
        row_iterator += 1

def update_ui():
    pass
