import tkinter as tk

def init_ui(size):
    global window
    global ui_board
    window = tk.Tk()
    # Fill UI board with zeroes
    ui_board = [[tk.Label(window,text="test") for i in range(size)] for j in range(size)]

def update_ui():
    pass
