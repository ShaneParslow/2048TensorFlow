import tkinter as tk

global colors
colors = {0:"#CCC0B3",2:"#EDE3DA",4:"#ECDFC8",8:"#F1B07C",16:"#F39568",32:"#F47D64",64:"#F46146"}

def init_ui(game):
    global window
    global ui_board
    window = tk.Tk()

    # Fill UI board with zeroes
    ui_board = [[tk.Label(window,text="0") for i in range(game.size)] for j in range(game.size)]
    # Setup geometry managers for each label in ui_board
    row_iterator = 0
    for row in ui_board:
        for label_iterator in range(0,len(row)):
            ui_board[row_iterator][label_iterator].grid(row=row_iterator,column=label_iterator,ipadx=10,ipady=10)
        row_iterator += 1
    # Bind arrow keys to shift board
    window.bind("<Up>", lambda a: game.shift_up())
    window.bind("<Right>", lambda a: game.shift_right())
    window.bind("<Down>", lambda a: game.shift_down())
    window.bind("<Left>", lambda a: game.shift_left())

def update_ui(game):
    row_iterator = 0
    # Update all labels with backend values
    for row in ui_board:
        for label_iterator in range(0,len(row)):
            new_value = game.board[row_iterator][label_iterator]
            try:
              ui_board[row_iterator][label_iterator].config(text=new_value,bg=colors[new_value])
            # If color is not in dictionary fallback to red
            except KeyError:
                ui_board[row_iterator][label_iterator].config(text=new_value,bg="#FF0000")
        row_iterator += 1
