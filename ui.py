import tkinter as tk

def init_ui(size):
    global window
    global ui_board
    window = tk.Tk()
    window.geometry("100x100")

    # Fill UI board with zeroes
    ui_board = [[tk.Label(window,text="0") for i in range(size)] for j in range(size)]
    # Setup geometry managers for each label in ui_board
    row_iterator = 0
    for row in ui_board:
        for label_iterator in range(0,len(row)):
            ui_board[row_iterator][label_iterator].grid(row=row_iterator,column=label_iterator)
        row_iterator += 1

def update_ui():
    pass
